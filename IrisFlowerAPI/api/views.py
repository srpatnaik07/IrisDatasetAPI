from django.shortcuts import render
import pandas as pd
import numpy as np
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class SpeciesPrediction(APIView):
    def post(self,request):
        data = request.data
        new_data = {'SepalLengthCm':data.get('SepalLengthCm'),
                    'SepalWidthCm':data.get('SepalWidthCm'),
                    'PetalLengthCm':data.get('PetalLengthCm'),
                    'PetalWidthCm':data.get('PetalWidthCm')}
        df = pd.DataFrame(new_data,index=[0])
        flower_classification = ApiConfig.model
        prediction = flower_classification.predict(df)
        species = prediction[0]

        return Response({'species':species})
    