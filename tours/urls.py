from django.urls import path
from .views import tours 

urlpatterns = [
    path('', tours, name='tours'),
]