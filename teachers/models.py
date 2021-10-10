from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=250)
    teacher_pic = models.ImageField(upload_to='photos/%Y/m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name