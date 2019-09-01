from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from .models import Tweet

User = get_user_model()


class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username="jtestUser33")

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content="Some random test content")
        self.assertTrue(obj.content == "Some random test content")
        self.assertTrue(obj.id == 1)
        absolute_url = reverse("tweet:detail", kwargs={"pk": 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
