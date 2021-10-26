from django.db import models
from django.contrib.auth.models import User
from datetime import date
from teachers.models import Teacher

# Create your models here.


class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    lessons = models.IntegerField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField(default=date.today, blank=True)
    main_pic = models.ImageField(upload_to='photos/%Y/m/%d/')
    pic_1 = models.ImageField(upload_to='photos/%Y/m/%d/', blank=True)
    pic_2 = models.ImageField(upload_to='photos/%Y/m/%d/', blank=True)
    pic_3 = models.ImageField(upload_to='photos/%Y/m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    students = models.ManyToManyField(
        User, related_name="user_courses", blank=True)

    def __str__(self):
        return self.title
