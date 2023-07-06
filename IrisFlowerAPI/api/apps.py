from django.apps import AppConfig
import os
import joblib
from django.conf import settings


class ApiConfig(AppConfig):
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS,"IrisFlowerClassification.joblib")
    model = joblib.load(MODEL_FILE)
    
