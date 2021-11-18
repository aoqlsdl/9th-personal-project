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
    return render(request, 'home.html', {'record': records})

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
    return render(request, 'new.html', {'form': form})


def create(request):   
    if request.method == "POST":
        form = RecordForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.pub_date = timezone.now()
            new_record.user_name = User.objects.get(id = User)
            new_record.save()
            new_record.image = request.FILES.get('image', '')
            for img in request.FILES.getlist('image'):
                photo = ImageUpload()
                photo.record = Record
                photo.image = img
                photo.save()
            hashtags = request.POST['hashtags']
            hashtag = hashtags.split(",")
            for tag in hashtag:
                ht = HashTag.objects.get_or_create(hashtag_name=tag)
                new_record.hashtag.add(ht[0])
        # return render(request, new_record.id)
        else:
            redirect('create')
    elif request.method == "GET":
        form = RecordForm()
        return render(request, 'new.html', {'form':form})
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

def scrap_record(request, record_id):
    record_detail = get_object_or_404(Record, pk=record_id)
    record_detail.like_users += 1
    record_detail.save()
    return detail(request, record_id)

# def index(request):
#     record = Record.objects.filter(
#         Q(user=request.user) | Q(user_id__in=request.user.followings.all())
#     )

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES["imgfile"]
        fileupload = FileUpload(
            title=title,
            content=content,
            imgfile=img,
        )
        fileupload.save()
        return redirect('fileupload')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'fileupload.html', context)

def portfolio_create(request):
    # 'extra' : number of photos
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES,)

        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            form.save_m2m() # tag를 저장하는 부분

#hash tag 검색
def hashtag(request):
    if request.method == 'POST':
        keyword = request.POST.get('search_button') # keyword를 입력받음
        tag = HashTag.objects.filter(hashtag_name=keyword) # 해당 키워드를 가진 tag 클래스 오픈
        post= Record.objects.filter(hashtag__in = tag).order_by('pub_date') # 해당 태그를 가진 post 저장

        # if post:
        #    post_ = post[0]
        # else:
        #    post_ = None

        return render(request, 'search_result.html', {'post':post, 'keyword':keyword})
    elif request.method == 'GET':
        return redirect('/')