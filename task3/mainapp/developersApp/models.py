from django.db import models
from django.contrib.auth.models import User


class Developer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    developers = models.ManyToManyField(
        "Developer", related_name="projects", blank=True
    )

    def __str__(self):
        return f"{self.title}"


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    developer = models.ForeignKey(
        Developer, on_delete=models.CASCADE, related_name="skills", blank=True
    )

    def __str__(self):
        return f"{self.title}"


# class userRegister(models.Model):
#     userName = models.CharField(max_length=100)
#     lastName = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     phoneNumber = models.CharField(max_length=11)
#     email = models.EmailField(max_length=100)
#     def __str__(self):
#         return self.userName

class profile(models.Model):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to="profilePic" ,blank=True , null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    def __str__(self):
        return self.user.username