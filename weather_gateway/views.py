from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from config import open_weather


def get_from_service(request, service):
    city = request.GET['city']
    api_url = service['api_url']
    token = service['api_token']
    return requests.get(
        api_url + f"?q={city}&appid={token}&units=metric")


class OpenWeatherView(APIView):
    def get(self, request):
        result = get_from_service(request, open_weather)
        data = result.json()
        return Response(data)
