from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet
# Create your views here.

# Retrieve


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Tweet.objects.get(id=pk)


class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # context["another_list"] = Tweet.objects.all()
        # print(context)
        return context


# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)  # get from db
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request, 'tweets/detail_view.html', context)


# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     for obj in queryset:
#         print(obj)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, 'tweets/list_view.html', context)
