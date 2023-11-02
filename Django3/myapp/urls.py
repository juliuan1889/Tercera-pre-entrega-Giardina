from django.urls import path
from myapp.views import inicio, saludo

urlpatterns = [
    path('', inicio),
    path('index/', saludo),
]
