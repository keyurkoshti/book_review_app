from django.urls import path
from .views import form_view, home

urlpatterns = [
    path('form/', form_view, name='form_view'),
    path('home/', home, name='home'),
]
