from django.db import models
import uuid
from django.contrib.auth.base_user import AbstractBaseUser


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
    
    article_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    article_title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    is_featured=models.BooleanField()
    total_comments=models.IntegerField()
    total_likes=models.IntegerField()
    status=models.IntegerField(choices=STATUS, default=0)
    # created_by = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.article_title


class Comments(models.Model):
    comment_id=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    commentator_id=models.UUIDField(editable=False, default=uuid.uuid4)
    comment=models.CharField(max_length=255)
    status=models.IntegerField(choices=CSTATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    user_id=models.UUIDField(editable=False, default=uuid.uuid4,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id

class Media(models.Model):
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    content_type=models.CharField(max_length=120)
    content_name=models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.content_name

# class Profile(AbstractBaseUser):

#     id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     username=models.CharField(max_length=20,unique=True)
#     email=models.CharField(max_length=150,unique=True)
#     is_active=models.BooleanField(default=True)
#     is_admin=models.BooleanField(default=False)
#     is_writer=models.BooleanField(default=False)
#     is_editor=models.BooleanField(default=False)
#     last_login=models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)  


#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.username