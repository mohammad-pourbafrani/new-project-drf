from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.title
