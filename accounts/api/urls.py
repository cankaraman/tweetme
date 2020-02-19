from django.conf.urls import url
from tweets.api.views import TweetListAPIView
# from django.views.generic.base import RedirectView
urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(), name='list'),
]
