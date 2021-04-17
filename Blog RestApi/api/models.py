from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Published"),
    (2,"Unpublished")
)

class Articles(models.Model):
    
    article_id=models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    article_title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    is_featured=models.BooleanField()
    total_comments=models.IntegerField()
    total_likes=models.IntegerField()
    status=models.IntegerField(choices=STATUS, default=0)
    created_by = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.article_title