from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        to=Post, related_name='comments', null=False, blank=False,
        on_delete=models.CASCADE)
    author_name = models.CharField(max_length=40)
    content = models.CharField(max_length=500)

    class Meta:
        ordering = ('-pk',)
