from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class ServicesData(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100)
    course_duration=models.CharField(max_length=100)
    course_start_date=models.DateField(max_length=100)
    course_start_time=models.TimeField(max_length=100)
    course_trainer_name=models.CharField(max_length=100)
    course_trainer_exp=models.IntegerField()

class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField(max_length=100)
    feedback=models.CharField(max_length=500)

class EnquiryData(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email = models.EmailField(max_length=100)
    gender=models.CharField(max_length=10)


    COURSE_CHOICES=(
        ('py','Python'),
        ('dj','Django'),
        ('st','Software Testing'),
        ('sql','SQL'),
        ('UI','UI')
    )
    course=MultiSelectField(choices=COURSE_CHOICES)
    SHIFTS_CHOICES=(
        ('Morning','Morning Shifts'),
        ('Afternoon','Afternoon Shifts'),
        ('Evening','Evening Shifts'),
        ('Night','Night Shifts')
    )
    shifts=MultiSelectField(choices=SHIFTS_CHOICES)
    start_date=models.DateTimeField(max_length=100)
