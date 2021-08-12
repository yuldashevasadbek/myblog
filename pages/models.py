from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db import models



# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])

