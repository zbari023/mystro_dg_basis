from django.db import models

# Create your models here.

class Autor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=15000)
    def __str__(self):
        return self.name
    
    
class mypost(models.Model):
    title = models.CharField(max_length=100)
    publishedDate = models.DateTimeField()
    content = models.TextField(max_length=15000)
    autor = models.ForeignKey(Autor,related_name='mypost_Autor',on_delete=models.CASCADE)
    def __str__(self):
        return self.title