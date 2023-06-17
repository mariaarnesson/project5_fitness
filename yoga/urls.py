from django.urls import path
from .views import PoseListView

urlpatterns = [
    # other paths
    path('poses/', PoseListView.as_view(), name='pose_list'),
]