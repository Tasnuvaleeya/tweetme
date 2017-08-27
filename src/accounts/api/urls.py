from django.conf.urls import url
# from .views import TweetDetailView, TweetListView,TweetCreateView,TweetUpdateView,TweetDeleteView
from django.views.generic.base import RedirectView
from tweets.api.views import TweetListAPIView

urlpatterns = [

    url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(),name='list'),


]