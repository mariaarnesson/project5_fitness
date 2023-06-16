from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class YogaPoses(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class YogaExercise(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    level = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    original_name = models.CharField(max_length=100)
    description = models.TextField()
    yoga_poses = models.ForeignKey('YogaPoses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class YogaDay(models.Model):
    quantity = models.PositiveIntegerField()
    yoga_exercise = models.ForeignKey('YogaExercise', on_delete=models.CASCADE)

    def __str__(self):
        return f"YogaDay {self.pk}"


class YogaWorkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yoga_exercises = models.ManyToManyField(YogaExercise)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"YogaWorkout {self.pk}"
