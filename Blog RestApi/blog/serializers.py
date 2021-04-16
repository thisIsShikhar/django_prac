from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('post_id', 'title', 'description', 'created_at', 'updated_at','total_comments')
        model = models.Post