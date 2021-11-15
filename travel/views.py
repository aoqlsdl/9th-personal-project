from datetime import time
from functools import reduce
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.db.models.fields.related import ManyToManyField
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForm, RecordForm, UploadForm
from travel.models import HashTag, Record, Comment, MyPage, ImageUpload


# Create your views here.


def home(request):
    records = Record.objects #query set
    return render(request, 'home.html', {'record': records, 'user_name': User})

def detail(request, record_id):
    record_detail = get_object_or_404(Record, pk = record_id)
    record_hashtag = record_detail.hashtag.all()
    if request.method == 'post':
        record_image = UploadForm(request.POST, request.FILES)
        if record_image.is_valid():
            record_image.save()
            return redirect('image_list')
    else:
        record_image = UploadForm()
    return render(request, 'detail.html', {'record': record_detail, 'hashtags': record_hashtag, 'images': record_image})

def new(request):
    form = RecordForm()
    return render(request, 'new.html')

def create(request):
    form = RecordForm(request.POST, request.FILES)
    if form.is_valid():
        new_record = form.save(commit=False)
        new_record.pub_date = timezone.now()
        new_record.user_name = form.save(commit=False)
        new_record.save()
        new_record.image = request.FILES.get('image')
        for img in request.FILES.getlist('image'):
            # Photo 객체를 하나 생성한다.
            photo = ImageUpload()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = Record
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
        hashtags = request.POST['hashtags']
        hashtag = hashtags.split(",")
        for tag in hashtag:
            ht = HashTag.objects.get_or_create(hashtag_name=tag)
            new_record.hashtag.add(ht[0])
            
        return render(request, new_record.id)
    return redirect('home') 
    


def delete(request, record_id):
    records = Record.objects.get(pk=record_id)
    records.delete()
    return redirect('home')

def edit(request, record_id):
    record_detail = get_object_or_404(Record, pk=record_id)
    return render(request, 'edit.html', {'record' : record_detail})

def update(request, record_id):
    record_update = get_object_or_404(Record, pk=record_id)
    record_update.title = request.POST['title']
    record_update.body = request.POST['body']
    record_update.save()
    return redirect('home')

def add_comment(request, record_id):
    record = get_object_or_404(Record, pk = record_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = record
            comment.save()
            return redirect('detail', record_id)

        else:
            form = CommentForm()
        return render(request, 'add_comment.html', {'form' : form})

def mypage(request):
    return render(request, 'mypage.html')

def like_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.user in record.like_users.all():
        record.like_users.remove(request.user)
    else:
        record.like_users.add(request.user)

def index(request):
    record = Record.objects.filter(
        Q(user=request.user) | Q(user_id__in=request.user.followings.all())
    )