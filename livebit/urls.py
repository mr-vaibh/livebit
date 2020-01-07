"""livebit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path,include

from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name='home'),
	path('upload', views.upload, name='upload'),
	path('search', views.search, name='search'),
	path('sign-up', views.signup),
	path('logout', views.logout),
	re_path(r'^(?P<username>[a-zA-Z0-9_]+)$', views.profile),
	path('ajax-sign-up', views.ajaxsignup),
	path('ajax-login', views.ajaxlogin),
	path('ajax-save-photo', views.ajaxsavephoto),
	path('ajax-set-profile-pic', views.ajaxsetprofilepic),
	path('ajax-profile-feed', views.ajaxprofilefeed),
	path('ajax-like-photo', views.ajaxlikephoto),
	path('ajax-follow', views.ajaxfollow),
	path('ajax-tag', views.ajaxtag),
	path('ajax-photo-feed', views.ajaxphotofeed)
]
