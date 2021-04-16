from django.db import models

class Post(models.Model):
    id=models.UUIDField(max_length=36)
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_featured=models.BooleanField()
    total_comments=models.IntegerField()
    total_likes=models.IntegerField()
    status=models.enums(DRAFT, PUBLISHED, UNPUBLISHED)
    created_by=models.UUIDField(max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title