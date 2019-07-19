from django.conf import settings
from django.db import models
from django.utils import timezone
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    maintext = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='static/media')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Order(models.Model):
    dops=models.TextField()
    tgid=models.CharField(max_length=200)
        
