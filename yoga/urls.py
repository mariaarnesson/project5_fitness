from django.urls import path
from . import views

urlpatterns = [
    path('poses/', views.poses_view, name='poses'),
    path('exercises/<int:pose_id>/', views.exercises_view, name='exercises')
]