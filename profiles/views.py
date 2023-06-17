from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required
def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    exercises_completed = user_profile.exercises_completed.all()
 

    return render(request, 'profile.html', {'exercises_completed': exercises_completed})