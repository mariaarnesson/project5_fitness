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
            reservation.user = request.user
            reservation.save()
            messages.success(
                request, 'Reservation request submitted succesfully.You can check you reservation at: My bookings'
                )
        else:
            messages.error(request, 'The table is already booked.')
            reservation = form.instance.date

    form = OnlineBookingForm()
    context = {
        'form': form,
    }
    return render(request, 'online_booking.html', context)


@login_required
def mybookings(request):
    try:
        online_bookings = get_list_or_404(OnlineBooking, user=request.user)
    except Exception:
        online_bookings = None

    form = OnlineBookingForm()
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


from django.contrib import messages

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
