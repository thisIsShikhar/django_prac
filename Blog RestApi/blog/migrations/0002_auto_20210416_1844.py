# Generated by Django 3.2 on 2021-04-16 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(default=25, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=23, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_id',
            field=models.UUIDField(default=23, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='total_comments',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='total_likes',
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
    ]
