from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import View
from .models import OnlineBooking
from .forms import OnlineBookingForm
from datetime import date
from django.contrib import messages
from django.utils.decorators import method_decorator


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html', {})


class ReservationView(View):

    def get(self, request):
        return render(request, 'reservation.html')


class MenuView(View):

    def get(self, request):
        return render(request, 'menu.html')


@method_decorator(login_required, name='dispatch')
class OnlineBookingView(View):

    template_name = 'online_booking.html'
    queryset = OnlineBooking.objects.filter(approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_tables = 30
        booked_tables = OnlineBooking.objects.count()
        available_tables = total_tables - booked_tables
        form = OnlineBookingForm()
        context['form'] = form
        context['available_tables'] = available_tables
        return context

    def post(self, request):
        form = OnlineBookingForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            if reservation.date < date.today():
                messages.error(request, 'You cannot book a table for a past date.')
                return redirect('online_booking')

            reservation.user = request.user
            reservation.approved = False
            reservation.save()
            messages.success(request, 'Reservation request submitted successfully. Your booking is pending approval.')
            return redirect('mybookings')
        else:
            messages.error(request, 'The table is already booked.')

        context = {
            'form': form,
        }
        return render(request, 'online_booking.html', context)

@method_decorator(login_required, name='dispatch')
class MyBookingsView(View):

    def get(self, request):
        online_bookings = OnlineBooking.objects.filter(user=request.user)
        context = {
            'online_bookings': online_bookings,
        }
        return render(request, 'mybookings.html', context)

@method_decorator(login_required, name='dispatch')
class EditBookingView(View):

    def get(self, request, booking_id):
        booking = get_object_or_404(OnlineBooking, id=booking_id, user=request.user)
        form = OnlineBookingForm(instance=booking)
        context = {
            'form': form,
        }
        return render(request, 'edit_booking.html', context)

    def post(self, request, booking_id):
        booking = get_object_or_404(OnlineBooking, id=booking_id, user=request.user)
        form = OnlineBookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('mybookings')

        context = {
            'form': form,
        }
        return render(request, 'edit_booking.html', context)

@method_decorator(login_required, name='dispatch')
class DeleteBookingView(View):

    def get(self, request, booking_id):
        booking = get_object_or_404(OnlineBooking, id=booking_id, user=request.user)
        context = {
            'booking': booking,
        }
        return render(request, 'delete_booking.html', context)

    def post(self, request, booking_id):
        booking = get_object_or_404(OnlineBooking, id=booking_id, user=request.user)
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('mybookings')
