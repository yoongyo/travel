from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=20)
    content = models.TextField()
    registed_at = models.DateField(auto_now_add=True)


