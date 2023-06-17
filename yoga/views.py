from django.shortcuts import render, get_object_or_404
from .models import YogaPoses, YogaExercise



def poses_view(request):
    poses = YogaPoses.objects.all()
    return render(request, 'poses.html', {'poses': poses})


def exercises_view(request, pose_id):
    pose = get_object_or_404(YogaPoses, pk=pose_id)
    exercises = pose.yogaexercise_set.all()
    return render(request, 'exercises.html', {'exercises': exercises})
