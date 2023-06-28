from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('online_booking/', views.OnlineBookingView.as_view(), name='online_booking'),
    path('contact-details/', views.ContactDetailsView.as_view(), name='contact_details'),
    path('mybookings/', views.MyBookingsView.as_view(), name='mybookings'),
    path('edit_booking/<int:booking_id>/', views.EditBookingView.as_view(), name='edit_booking'),
    path('delete_booking/<int:booking_id>/', views.DeleteBookingView.as_view(), name='delete_booking'),
]
