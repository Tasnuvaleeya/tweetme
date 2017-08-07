# from django.contrib import admin
from django.conf.urls import url
# from .views import tweet_list_view,tweet_detail_view
from .views import TweetDetailView, TweetListView,TweetCreateView,tweet_create_view

urlpatterns = [
    url(r'^$',TweetListView.as_view(),name='list'),
    # url(r'^create/$',TweetCreateView.as_view(), name='create'),
    url(r'^create/$',tweet_create_view, name='create'),
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(), name='detail'),

]