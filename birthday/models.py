from django.db import models

class Birthday(models.Model):
    name = models.CharField(max_length= 200)
    description= models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.name
