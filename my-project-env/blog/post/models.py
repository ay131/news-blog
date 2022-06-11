from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here..
# user- title- img -content -creatd

class post (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField(default=' ')
    img=models.ImageField(default='download.png',upload_to='post_img/')
    created=models.DateTimeField(default = timezone.now )


    def __str__(self):
        return (self.title)
