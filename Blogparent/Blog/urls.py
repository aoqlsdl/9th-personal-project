"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

import blogapp.views as blogapp
import account.views as account
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.home, name="home"),
    path('blog/<int:blog_id>', blogapp.detail, name="detail"),
    path('new/', blogapp.new, name="new"),
    path('create/', blogapp.create, name="create"),
    path('edit/<int:blog_id>', blogapp.edit, name="edit"),
    path('update/<int:blog_id>', blogapp.update, name="update"),
    path('delete/<int:blog_id>', blogapp.delete, name="delete"),
    path('<int:blog_id>/comment', blogapp.add_comment_to_post, name="add_comment_to_post"),
    path('account/login', account.login_view, name="login"),
    path('account/logout', account.logout_view, name="logout"),
    path('account/register', account.register_view, name="register"),
    path('edit_user_info/', account.edit_user_info, name='edit_user_info'),
    path('<int:blog_id>/create_youtube', blogapp.create_youtube, name="create_youtube"),
    path('delete/<int:blog_id>/<int:youtube_id>', blogapp.delete_youtube, name="delete_youtube"),
    path('edit/<int:blog_id>/<int:youtube_id>', blogapp.edit_youtube, name="edit_youtube"),
    path('update_youtube/<int:youtube_id>', blogapp.update_youtube, name="update_youtube"),
    path('video_list/', blogapp.video_list, name="video_list"),
    path('mypage/', blogapp.mypage, name="mypage"),
    path('delete_comment/<int:blog_id>/<int:comment_id>', blogapp.delete_comment, name="delete_comment"),
    path('edit_comment/<int:blog_id>/<int:comment_id>', blogapp.edit_comment, name="edit_comment"),
    path('update_comment/<int:comment_id>', blogapp.update_comment, name="update_comment"),
    path('like/', blogapp.likes, name="likes"), #좋아요
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
