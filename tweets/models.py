from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import post_save
import re

from .validators import validate_content
from hashtags.signals import parsed_hashtags


class TweetManager(models.Manager):
    def retweet(self, user, parent_obj):
        # in case of retweet of retweet: retweet original tweet not the retweet
        # itself
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        # don't let retweeting of same tweet by same user
        qs = self.get_queryset().filter(user=user, parent=og_parent)
        if qs.exists():
            return None

        obj = self.model(
            parent=og_parent,
            user=user,
            content=parent_obj.content,
        )
        obj.save()
        return obj

    def like_toggle(self, user, tweet_obj):
        if user in tweet_obj.liked.all():
            is_liked = False
            tweet_obj.liked.remove(user)
        else:
            is_liked = True
            tweet_obj.liked.add(user)
        return is_liked


class Tweet(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True)
    content = models.CharField(max_length=140, validators=[validate_content])
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="liked")
    updated = models.DateTimeField(auto_now=True)
    reply = models.BooleanField(verbose_name="Is a reply?", default=False)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    objects = TweetManager()

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={'pk': self.pk})

    class Meta:
        ordering = ["-timestamp"]

    # validation in db
    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "dbc":
    #         raise ValidationError("Cannot be ABC")
    #     return super(Tweet, self).clean(*args, **kwargs)


def tweet_save_receiver(sender, instance, created, *args, **kwargs):
    if created and not instance.parent:
        # notify user
        user_regex = r"@(?P<username>[\w.@+-]+)"
        usernames = re.findall(user_regex, instance.content)
        # send user notification here

        hash_regex = r"#(?P<hashtag>[\w\d-]+)"
        hashtags = re.findall(hash_regex, instance.content)
        # send user notification hashtag here
        parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)

        [usernames, hashtags]


post_save.connect(tweet_save_receiver, sender=Tweet)
