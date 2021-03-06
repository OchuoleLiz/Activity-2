from django.db import models
from django.db.models.fields.files import ImageField
from django.utils import timezone
from django.conf import settings
import os

# Create your models here.
def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    content = models.TextField()
    published_date = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=100, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
