from .views import UserDetailView

from django.conf.urls import url
from django.views.generic.base import RedirectView

urlpatterns=[
    url(r'^(?P<username>[\w.@+-]+)/$',UserDetailView.as_view(),name='detail'),
]