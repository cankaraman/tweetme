from django.db.models import Q
from rest_framework import generics

from tweets.models import Tweet
from tweets.api.pagination import StandardResultPagination
from tweets.api.serializers import TweetModelSerializer
from hashtags.models import HashTag


class HashTagAPIView(generics.ListAPIView):
    queryset = Tweet.objects.all().order_by("-timestamp")
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultPagination

    def get_serializer_contex(self, *args, **kwargs):
        context = super(HashTagAPIView, self).get_serializer_context(*args, **kwargs)
        context["request"] = self.request

    def get_queryset(self, *args, **kwargs):
        hashtag = self.kwargs.get("hashtag")
        hashtag_obj = HashTag.objects.get_or_create(tag=hashtag)[0]

        if hashtag_obj:
            qs = hashtag_obj.get_tweets()
            query = self.request.GET.get("q", None)
            if query is not None:
                qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                )
            return qs
        return None
