from django.conf.urls import url
from .views import TweetListAPIView, TweetCreateAPIView, RetweetAPIView, LikeToggleAPIView
# from django.views.generic.base import RedirectView
urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'),
    url(r'^create$', TweetCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),  # tweet/api/id/retweet
    url(r'^(?P<pk>\d+)/like/',  LikeToggleAPIView.as_view(), name='like-toggle'),  # tweet/api/id/retweet
]
