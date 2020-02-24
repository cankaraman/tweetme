from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
# Create your views here.

# Retrieve


class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated():
            # new_tweet =
            Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect("/")  # new_tweet.get_absolute_url())
        return HttpResponseRedirect(tweet.get_absolute_url())


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = reverse_lazy("tweet:update")
    # login_url = "/admin/"
    # fields = ["user","content"]


class TweetUpdateView(UserOwnerMixin, LoginRequiredMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = "/tweet/"


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # template_name = 'tweets/tweet_detail.html'

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Tweet.objects.get(id=pk)


class TweetListView(LoginRequiredMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # context["another_list"] = Tweet.objects.all()
        # print(context)
        context["create_form"] = TweetModelForm()
        context["create_url"] = reverse_lazy("tweet:create")
        return context


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("tweet:list")


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
