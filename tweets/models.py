from django.db import models
from django.conf import settings
from .validators import validate_content
from django.urls import reverse


class Tweet(models.Model):
    content = models.CharField(max_length=140, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

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
