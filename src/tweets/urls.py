# from django.contrib import admin
from django.conf.urls import url
from .views import tweet_list_view,tweet_detail_view

urlpatterns = [
    url(r'^$', tweet_list_view, name='list'),
    url(r'^1/$', tweet_detail_view, name='detail')
]