from django.conf.urls import url
from .views import TweetListAPIview
# from django.views.generic.base import RedirectView
urlpatterns = [
    url(r'^$', TweetListAPIview.as_view(), name='list'),
]
