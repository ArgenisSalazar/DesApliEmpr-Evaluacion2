from django.urls import path
from .views import all_Libro

urlpatterns = [
    path('',all_Libro,name='all_Libro'),
]