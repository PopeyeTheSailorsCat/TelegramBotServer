from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

open_weather_token = "9bf05fd8bdd48497c327eb13ac7727fd"


class OpenWeatherView(APIView):
    def get(self, request):
        city = request.GET['city']
        result = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = result.json()
        return Response(data)
