from django.db import models

 
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    skills = models.TextField()
    description = models.TextField()
    github_repo = models.CharField(max_length=200)
    education = models.JSONField(encoder=None)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"