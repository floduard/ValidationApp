from django.urls import path
from valide.views import HomeView, ParticipantFormView, VehicleFormView, SuccessView, ParticipantListView, VehicleListView

urlpatterns = [
    path('add_participant/', ParticipantFormView.as_view(), name='participant_form'),
    path('', HomeView.as_view(), name='home'), 
    path('participant-form/', ParticipantFormView.as_view(), name='participant_form'),
    path('vehicle-form/', VehicleFormView.as_view(), name='vehicle_form'),
    path('success/', SuccessView.as_view(), name='success'),
    path('participant-list/', ParticipantListView.as_view(), name='participant_list'),
    path('vehicle-list/', VehicleListView.as_view(), name='vehicle_list'),
]
