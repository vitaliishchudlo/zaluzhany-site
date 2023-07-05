from django.db import models
from django.utils import timezone
import os

def get_image_path(instance, filename):
    # Function to determine the path to save the image
    # Uses the app name "news" in the path for each image
    return os.path.join('news', str(instance.id), filename)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=get_image_path)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
