from django.views.generic import ListView
from .models import YogaExercise

class PoseListView(ListView):
    model = YogaExercise
    template_name = 'pose_list.html'
    context_object_name = 'yoga_exercises'