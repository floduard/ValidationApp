# validationApp/views.py
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import ParticipantAdminForm, vehicle1Form, vehicleForm
from .models import Participant, vehicle
from datetime import datetime
from django.views.generic.edit import CreateView


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)



class ParticipantFormView(View):
    template_name = 'participant_form_admin.html'
    form_class = ParticipantAdminForm 
    vehicle1Form = vehicle1Form

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form,'vehicle1Form':vehicle1Form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
        return render(request, self.template_name, {'form': form})

class vehicleFormView(View):
    template_name = 'vehicle_form.html'
    form_class = vehicleForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_form')
        return render(request, self.template_name, {'form': form})
class vehicle1FormView(View):
    template_name = 'vehicle_form.html'
    form_class = vehicle1Form

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_form')
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

class vehicleListView(View):
    template_name = 'vehicle_list.html'

    def get(self, request):
        vehicles = vehicle.objects.all()
        return render(request, self.template_name, {'vehicles': vehicles})
