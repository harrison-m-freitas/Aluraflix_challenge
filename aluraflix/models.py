from django.db import models
from django.urls import reverse


class Category(models.Model):
    
    title = models.CharField(max_length=150)
    color = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("categories-detail", kwargs={"pk": self.pk})


def get_default_categoty():
    """ get a default value for category; create new status if not available """
    return Category.objects.get_or_create(title="LIVRE", defaults={"color": "WHITE"})[0]

# Create your models here.
class Video(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField()
    url = models.URLField()
    
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=get_default_categoty)
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
            return reverse("videos-detail", kwargs={"pk": self.pk})
