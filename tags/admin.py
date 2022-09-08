from django.contrib import admin
from .models import Tag, TaggedItem, LikedItem

# Register your models here.
admin.site.register(Tag)
admin.site.register(TaggedItem)
admin.site.register(LikedItem)