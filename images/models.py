from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

def user_directory_path(instance, filename):
    return 'images+/{0}/'.format(filename)

class Category(models.Model):
    name = models.CharField(max_length=200)
    profile = models.CharField(default='', max_length=500)

    def __str__(self):
        return self.name

class Image(models.Model):

    option = (
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    alt = models.TextField(null=True)
    image = models.ImageField(
        upload_to=user_directory_path, default='posts/defualt.jpg'
    )
    slug = models.SlugField(max_length=250, unique_for_date='created')
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='author'
    )
    status = models.CharField(max_length=11, choices=option, default='active')
