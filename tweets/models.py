from django.db import models
from django.conf import settings
from .validators import validate_content
from django.urls import reverse


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


class Tweet(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True)
    content = models.CharField(max_length=140, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
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
