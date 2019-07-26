"""mygame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
from django.conf.urls import url, include
from mygame.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from apps.autoAdmin.urls import auto_router, auto_urls, sock_urls


urlpatterns = [
    url('^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url('^auto/', include(auto_router.urls)),
    url('^mock/', include(auto_urls)),
    url('^sock/(\d+)/', include(sock_urls)),
    url(r'docs/', include_docs_urls(title='game_doc')),

    url(r'^api-auth/', include('rest_framework.urls'))
]
