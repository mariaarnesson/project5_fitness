from django.db import models
from django.contrib.auth.models import User
from yoga.models import YogaExercise
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exercises_completed = models.ManyToManyField(YogaExercise, blank=True)
    photo = CloudinaryField('photo', blank=True, null=True)

    def __str__(self):
        return self.user.username