from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_id=models.UUIDField(max_length=36,primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    is_featured=models.BooleanField(default=True)
    total_comments=models.IntegerField()
    total_likes=models.IntegerField()
    # status=models.enums(DRAFT, PUBLISHED, UNPUBLISHED)
    created_by=models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title