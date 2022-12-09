from django.db import models
from blog.models import Blog
# Create your models here.


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=202)
    email = models.EmailField()
    website = models.CharField(max_length=202)
    message = models.TextField()

    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name