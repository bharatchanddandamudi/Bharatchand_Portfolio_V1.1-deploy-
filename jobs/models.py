from django.db import models
from django.urls import reverse



# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=5000)
   # video = models.FileField(upload_to='images/',null=True) 

    def __str__(self):
        return self.summary
    
    
def get_absolute_url(self):
    return reverse('links', kwargs={"pk": self.pk})