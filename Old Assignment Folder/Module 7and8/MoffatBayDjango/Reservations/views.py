from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from .models import Reservation
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Rooms.models import Room
from .forms import ReservationForm

# Create your views here.

class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'reservations/reservation_list.html'
    context_object_name = 'reservations'
    ordering = ['-created_at',]

    def get_uer_reservations(self):
        return Reservation.objects.filter(user_id=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = self.get_uer_reservations()
        return context

class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'reservations/reservation_detail.html'
    context_object_name = 'reservation'

class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/book.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_type'] = 'book'
        context['rooms'] = Room.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user

        room = form.cleaned_data['room_type_id']
        check_in = form.cleaned_data['check_in_date']
        check_out = form.cleaned_data['check_out_date']
        guests = form.cleaned_data['number_of_guests']
        form.instance.total_price = room.base_price * (check_out - check_in).days
        form.instance.reservation_status = 'Incomplete'
        if check_in >= check_out:
            form.add_error('check_out_date', 'Check out date must be after check in date')
            return self.form_invalid(form)
        
        if guests > room.max_occupancy:
            form.add_error('number_of_guests', 'Number of guests exceeds room capacity')
            return self.form_invalid(form)
        
        save = super().form_valid(form)
        return redirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('reservation-summary', kwargs={'pk': self.object.pk})

        
class ReservationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/book.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_type'] = 'update'
        context['rooms'] = Room.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user

        room = form.cleaned_data['room_type_id']
        check_in = form.cleaned_data['check_in_date']
        check_out = form.cleaned_data['check_out_date']
        guests = form.cleaned_data['number_of_guests']
        form.instance.total_price = room.base_price * (check_out - check_in).days
        form.instance.reservation_status = 'Incomplete'
        if check_in >= check_out:
            form.add_error('check_out_date', 'Check out date must be after check in date')
            return self.form_invalid(form)
        
        if guests > room.max_occupancy:
            form.add_error('number_of_guests', 'Number of guests exceeds room capacity')
            return self.form_invalid(form)
        
        save = super().form_valid(form)
        return redirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('reservation-summary', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        reservation = self.get_object()
        if self.request.user == reservation.user_id:
            return True
        return False
    
class ReservationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    print("Not implemented")
    
class ReservationSummaryView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'reservations/reservation_summary.html'
    context_object_name = 'reservation'

    def get_reservation(self, **kwargs):
        return Reservation.objects.get(pk=self.kwargs['pk'])
    
    
class ReservationConfirmView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        reservation = Reservation.objects.get(pk=self.kwargs['pk'])
        reservation.reservation_status = 'Confirmed'
        reservation.save()
        return redirect('reservation-detail', pk=reservation.pk)
    

class ReservationCancelView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        reservation = Reservation.objects.get(pk=self.kwargs['pk'])
        reservation.reservation_status = 'Cancelled'
        reservation.save()
        return redirect('home')
    
class ReservationEditView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        reservation = Reservation.objects.get(pk=self.kwargs['pk'])
        return redirect('reservation-update', pk=reservation.pk)