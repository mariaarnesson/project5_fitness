from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from yoga.models import YogaExercise
from .forms import ProfileForm


@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile')
    else:
        form = ProfileForm(instance=user_profile)

    exercises_completed = user_profile.exercises_completed.all()

    return render(request, 'profile.html', {'form': form, 'exercises_completed': exercises_completed})

@login_required
def exercises_completed_view(request, exercise_id):
    exercise = get_object_or_404(YogaExercise, id=exercise_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    user_profile.exercises_completed.add(exercise)
    return redirect('profiles:profile')