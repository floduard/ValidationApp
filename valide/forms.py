# validationApp/forms.py
from datetime import date
from django import forms
from .models import Participant, vehicle

# validationApp/forms.py
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Participant, vehicle

class ParticipantAdminForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
             'email': forms.EmailInput(attrs={'placeholder': 'example@ur.ac.rw'}),
             'phone':forms.TextInput(attrs={'placeholder':'+2507............'})
             
        }
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            age = date.today().year - date_of_birth.year - ((date.today().month, date.today().day) < (date_of_birth.month, date_of_birth.day))
            if age < 18:
                raise forms.ValidationError("Participants must be at least 18 years old.")
        return date_of_birth

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
             'email': forms.EmailInput(attrs={'placeholder': 'example@ur.ac.rw'}),
             'phone':forms.TextInput(attrs={'placeholder':'+2507............'})
        }
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            age = date.today().year - date_of_birth.year - ((date.today().month, date.today().day) < (date_of_birth.month, date_of_birth.day))
            if age < 18:
                raise forms.ValidationError("Participants must be at least 18 years old.")
        return date_of_birth
class vehicleForm(forms.ModelForm):
    class Meta:
        model = vehicle
        fields = '__all__'
        widgets = {
            'manufacture_date': forms.DateInput(attrs={'type': 'date'}),
        }
class vehicle1Form(forms.ModelForm):
    class Meta:
        model = vehicle
        fields = '__all__'
        widgets = {
            'manufacture_date': forms.DateInput(attrs={'type': 'date'}),
        }

