from django.urls import path
from .views import HomeView, ParticipantFormView, vehicleFormView, SuccessView, ParticipantListView, vehicleListView

urlpatterns = [
    path('add_participant/', ParticipantFormView.as_view(), name='participant_form'),
    path('', HomeView.as_view(), name='home'), 
    path('participant-form/', ParticipantFormView.as_view(), name='participant_form'),
    path('vehicle-form/', vehicleFormView.as_view(), name='vehicle_form'),
    path('success/', SuccessView.as_view(), name='success'),
    path('participant-list/', ParticipantListView.as_view(), name='participant_list'),
    path('vehicle-list/', vehicleListView.as_view(), name='vehicle_list'),
]
