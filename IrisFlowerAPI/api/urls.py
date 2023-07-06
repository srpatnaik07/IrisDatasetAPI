from django.urls import path
from .views import SpeciesPrediction

urlpatterns = [
    path('species/',SpeciesPrediction.as_view(),name='species_predicted')
]