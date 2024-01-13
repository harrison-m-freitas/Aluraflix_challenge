from django.db import models
from django.urls import reverse


# Create your models here.
class Video(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
            return reverse("videos-detail", kwargs={"pk": self.pk})

