from distutils.command.upload import upload
from email.mime import image
from turtle import title
from unittest.util import _MAX_LENGTH
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(
        upload_to='images/', validators=[FileExtensionValidator(['png', 'jpg'])], null=True, blank=True)

    metadata = models.FileField(upload_to='files/', blank=True, null=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):  # PostModel의 title을 admin에 넘겨주기 위해서 만듬
        return self.title


# class Photo(models.Model):
#     post = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(
#         upload_to='images/', validators=[FileExtensionValidator(['png', 'jpg'])], null=True, blank=True)

#     def __str__(self):
#         return self.image


# class File(models.Model):
#     post = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=True)
#     metadata = models.FileField(upload_to='files/', blank=True, null=True)

    # def __str__(self):
    #     return self.metadata
