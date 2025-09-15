from django.db import models

class Developers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name}"
    
    
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title}"



class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title}"
    