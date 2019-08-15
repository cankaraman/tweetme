# from .views import tweet_detail_view, tweet_list_view
from .views import TweetDetailView, TweetListView
from django.conf.urls import url

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
]
