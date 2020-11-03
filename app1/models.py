from django.db import models

from embed_video.fields import EmbedVideoField

# Create your models here.

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()


class student(models.Model):
    sname=models.CharField(max_length=25,primary_key=True)
    sfathername=models.CharField(max_length=25)
    sdob=models.DateField(auto_now=True)
    saadharno=models.CharField(max_length=15)
    smothername=models.CharField(max_length=25)
    sschoolname=models.CharField(max_length=50)
    sgrade=models.FloatField()
    scollegename=models.CharField(max_length=50)
    smarks=models.IntegerField()
    shouseno=models.CharField(max_length=50)
    scolonyname=models.CharField(max_length=50)
    scityname=models.CharField(max_length=50)
    sdistrictname=models.CharField(max_length=50)
    smandalname=models.CharField(max_length=50)
    sphonenumber=models.CharField(max_length=20)
    sgmail=models.EmailField()
    gender=models.CharField(max_length=25)
    degreegroup=models.CharField(max_length=25)
    board=models.CharField(max_length=25)
    intergroup=models.CharField(max_length=25)
    country=models.CharField(max_length=25)
    code=models.CharField(max_length=25)

    
class studentmessage(models.Model):
    sfname=models.CharField(max_length=25)
    slname=models.CharField(max_length=25)
    email=models.EmailField()
    subject=models.CharField(max_length=25)
    message=models.TextField(max_length=25)
    
    
    
