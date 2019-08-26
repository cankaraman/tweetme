# from .views import tweet_detail_view, tweet_list_view
from .views import TweetDetailView, TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView
from django.conf.urls import url

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete', TweetDeleteView.as_view(), name='delete'),
]
