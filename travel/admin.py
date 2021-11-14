from django.contrib import admin
from .models import *

class Photo(admin.TabularInline):
    model = ImageUpload

class RecordAdmin(admin.ModelAdmin):
    inlines = [Photo, ]

# Register your models here.
admin.site.register(HashTag)
admin.site.register(Record)
admin.site.register(Comment)
admin.site.register(MyPage)
admin.site.register(ImageUpload)