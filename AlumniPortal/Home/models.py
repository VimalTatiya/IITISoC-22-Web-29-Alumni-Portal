
from django.utils import timezone
from django.db import models


# Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=50)
    start_date=models.DateField()
    start_time=models.TimeField()
    finish_date=models.DateField()
    finish_time=models.TimeField()
    event_city=models.CharField(max_length=40)
    class Meta:
            verbose_name = 'Event'
            verbose_name_plural = 'Events'
    def __str__(self):
        return self.event_name       


class Info(models.Model):
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    email=models.EmailField()
    current_city=models.CharField(max_length=50)
    yog=models.CharField(max_length=10)
    contact=models.CharField(max_length=12)
    password=models.CharField(max_length=50)
    status=models.TextField(max_length=400)
    rollnum=models.CharField(max_length=15 , primary_key='true')
    class Meta:
        verbose_name='Info'
        verbose_name_plural='Info'
    def __str__(self):
        return self.name    

class Story(models.Model):
    uploadedBy=models.CharField(max_length=15,verbose_name='Name')
    story_name=models.CharField(max_length=50)
    story=models.TextField(max_length=1000)
    magzine=models.FileField()
    insti_update=models.TextField(max_length=1000)
    gallery=models.ImageField
    achievements=models.TextField(max_length=1000)
    class Meta:
        verbose_name='Story'
        verbose_name_plural='Stories'
    def __str__(self):
        return self.story_name   



