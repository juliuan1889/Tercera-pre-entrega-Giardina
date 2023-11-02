from django.urls import path
from myapp.views import productoFomulario

urlpatterns = [
    path('', productoFomulario),
]
