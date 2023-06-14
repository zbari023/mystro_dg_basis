from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Autor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=15000)
    image = models.ImageField(upload_to='autor')
    def __str__(self):
        return self.name
    
    
class mypost(models.Model):
    title = models.CharField(max_length=100)
    publishedDate = models.DateTimeField()
    content = models.TextField(max_length=15000)
    image = models.ImageField(upload_to='post')
     
    autor = models.ForeignKey(Autor,related_name='mypost_Autor',on_delete=models.CASCADE)
    
    tags = TaggableManager()
    def __str__(self):
        return self.title