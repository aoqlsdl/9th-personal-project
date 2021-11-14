"""personalproj URL Configuration

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
from django.urls import path, include
from travel import views as travel
from account import views as accounts
from django.conf.urls.static import static
from django.conf import settings
import map.views 

app_name = 'posts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', travel.home, name="home"),
    path('travel/<int:record_id>', travel.detail, name="detail"),
    path('travel/new/', travel.new, name="new"),
    path('travel/create/', travel.create, name="create"),
    path('travel/delete/<int:record_id>', travel.delete, name="delete"),
    path('accounts/login', accounts.login_view, name='login'),
    path('accounts/logout', accounts.logout_view, name="logout"),
    path('accounts/signup', accounts.register_view, name="register"),
    path('travel/edit/<int:record_id>', travel.edit, name="edit"),
    path('travel/update/<int:record_id>', travel.update, name="update"),
    path('<int:record_id>/comment', travel.add_comment, name='add_comment'),
    path('travel/mypage/', travel.mypage, name="mypage"),
    path('map/', map.views.map, name="map"),
    path('like/<int:record_id>/', travel.like_record, name="like_record"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
