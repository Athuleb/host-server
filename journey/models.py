from django.db import models

class DestinationImages(models.Model):
    dest_images = models.ImageField(upload_to='Topdestinations/')
    location = models.CharField(max_length=100,unique=True)
    dest_describe = models.TextField()
    def __str__(self):
        return f"Image {self.id} - {self.dest_images.name}" 
class Gallery(models.Model):
        image = models.ImageField(upload_to='gallery/')
