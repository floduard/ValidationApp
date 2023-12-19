# validationApp/views.py
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import ParticipantAdminForm, ParticipantForm, VehicleForm, ParticipantWithVehicleForm
from .models import Participant, Vehicle
from datetime import datetime
from django.views.generic.edit import CreateView


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class ParticipantCreateView(CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'participant_form.html'
    success_url = reverse_lazy('your_success_url')  # Replace with the actual success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VehicleFormSet = formset_factory(VehicleForm, extra=1, prefix='vehicle')
        context['vehicle_formset'] = VehicleFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        vehicle_formset = context['vehicle_formset']

        if form.is_valid() and vehicle_formset.is_valid():
            self.object = form.save()
            vehicle_formset.instance = self.object
            vehicle_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, vehicle_formset=vehicle_formset))

class ParticipantFormView(View):
    template_name = 'participant_form.html'
    form_class = ParticipantForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
        return render(request, self.template_name, {'form': form})

class ParticipantFormView(View):
    template_name = 'participant_form_admin.html'
    form_class = ParticipantAdminForm 
    VehicleForm = VehicleForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form,'VehicleForm':VehicleForm})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
        return render(request, self.template_name, {'form': form})

class VehicleFormView(View):
    template_name = 'vehicle_form.html'
    form_class = VehicleForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_form')
        return render(request, self.template_name, {'form': form})

class ParticipantWithVehicleFormView(View):
    template_name = 'participant_form_with_vehicle.html'
    form_class = ParticipantWithVehicleForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        return render(request, self.template_name, {'form': form})

class SuccessView(View):
    template_name = 'success.html'

    def get(self, request):
        return render(request, self.template_name)

class ParticipantListView(View):
    template_name = 'participant_list.html'

    def get(self, request):
        participants = Participant.objects.all()
        return render(request, self.template_name, {'participants': participants})

class VehicleListView(View):
    template_name = 'vehicle_list.html'

    def get(self, request):
        vehicles = Vehicle.objects.all()
        return render(request, self.template_name, {'vehicles': vehicles})
