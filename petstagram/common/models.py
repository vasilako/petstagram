from django.contrib.auth.models import User
from django.db import models

from petstagram.photos.models import Photos


# Create your models here.
class Comment(models.Model):
    user_comment = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    photo_comment = models.ForeignKey(
        Photos,
        on_delete=models.CASCADE
    )

    comment_tex = models.TextField(

    )

    date_time = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.user_comment}, {self.photo_comment}, {self.date_time}'

class Likes(models.Model):
    user_like = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    photo_like = models.ForeignKey(
        Photos,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user_like}, {self.photo_like}'