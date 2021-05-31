from django.urls import path
from .views import OpenWeatherView
app_name = "weather_gateway"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('openweather/', OpenWeatherView.as_view()),
]