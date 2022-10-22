from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_author')
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news_category')
    likes = models.ManyToManyField(User, related_name='news_likes', blank=True, null=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()