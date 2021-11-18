from django.urls import path

from .views import create_short_URL, redirect_from_short_to_long_URL


urlpatterns = [
    path('create', create_short_URL, name='create'),
    path('s/<str:short_url>', redirect_from_short_to_long_URL, name='redirect'),
]