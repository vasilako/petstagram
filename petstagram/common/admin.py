from django.contrib import admin

from petstagram.common.models import Comment, Likes


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    pass
