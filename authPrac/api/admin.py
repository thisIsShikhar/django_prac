from django.contrib import admin
from api.models import Articles, Comments, Likes, Media

admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Media)
