from django.shortcuts import render, redirect, HttpResponse, get_list_or_404, \
    get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OnlineBooking
from .forms import OnlineBookingForm
from datetime import date
from django.contrib import messages
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {})


def reservation(request):
    return render(request, 'reservation.html')


def menu(request):
    return render(request, 'menu.html')


@login_required    
def online_booking(request):

    if request.method == 'POST':
        form = OnlineBookingForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)

             # Check if the selected date is in the past
            if reservation.date < date.today():
                messages.error(request, 'You cannot book a table for a past date.')
                return redirect('online_booking')

            reservation.user = request.user
            reservation.approved = False
            reservation.save()
            messages.success(
                request, 'Reservation request submitted successfully. Your booking is pending approval.'
            )
            return redirect('mybookings')
        else:
            messages.error(request, 'The table is already booked.')
    else:
        form = OnlineBookingForm()

    context = {
        'form': form,
    }
    return render(request, 'online_booking.html', context)        


@login_required
def mybookings(request):
    try:
        online_bookings = get_list_or_404(OnlineBooking, user=request.user, approved=True)
    except Exception:
        online_bookings = None

 #   form = OnlineBookingForm()
    context = {
        'online_bookings': online_bookings,
    }
    return render(request, 'mybookings.html', context)

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(OnlineBooking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = OnlineBookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('mybookings')
    else:
        form = OnlineBookingForm(instance=booking)

    context = {
        'form': form,
    }
    return render(request, 'edit_booking.html', context)




@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(OnlineBooking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('mybookings')

    context = {
        'booking': booking,
    }
    return render(request, 'delete_booking.html', context)
