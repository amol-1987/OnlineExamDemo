from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomerAccount(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.CharField(max_length=1, choices=(
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('A', 'Admin'),
    ))

    def __str__(self):
        return self.user.username

class Exam(models.Model):
    name=models.CharField(max_length=100)
    marks=models.PositiveIntegerField()
    time=models.DateTimeField()

    def __str__(self):
        return self.name

class Question(models.Model):
    exam=models.ForeignKey(Exam, on_delete=models.CASCADE)
    question=models.CharField(max_length=200)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    ans=models.CharField(max_length=100, choices=(
                                                    ('A',option1),
                                                    ('B',option2),
                                                    ('C',option3),
                                                    ('D',option4),
                                                    ))
    def __str__(self):
        return self.question
