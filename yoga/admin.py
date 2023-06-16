from django.contrib import admin
from .models import YogaPoses, YogaExercise, YogaDay, YogaWorkout

admin.site.register(YogaPoses)
admin.site.register(YogaExercise)
admin.site.register(YogaDay)
admin.site.register(YogaWorkout)
