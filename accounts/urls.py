# from .views import tweet_detail_view, tweet_list_view
from .views import (
    UserDetailView,
    UserFollowView
)
from django.conf.urls import url, include

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),
]
