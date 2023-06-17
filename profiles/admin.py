from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_exercises_completed_count')

    def get_exercises_completed_count(self, obj):
        return obj.exercises_completed.count()

    get_exercises_completed_count.short_description = 'Exercises Completed'
