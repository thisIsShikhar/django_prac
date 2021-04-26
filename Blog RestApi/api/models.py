from django.db import models
import uuid

STATUS = (
    (0,"Draft"),
    (1,"Published"),
    (2,"Unpublished")
)

CSTATUS = (
    (0,"Published"),
    (1,"Unpublished")
)

class Articles(models.Model):
    
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    article_title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    is_featured=models.BooleanField()
    total_comments=models.IntegerField()
    total_likes=models.IntegerField()
    status=models.IntegerField(choices=STATUS, default=0)
    created_by = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.article_title


class Comments(models.Model):
    comment_id=models.UUIDField()
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    commentator_id=models.UUIDField()
    comment=models.CharField(max_length=255)
    status=models.IntegerField(choices=CSTATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article_title

class Likes(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    user_id=models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article_title

class Media(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    content_type=models.CharField(max_length=120)
    content_name=models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.article_title