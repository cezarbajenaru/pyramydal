from django.urls import path
from .views import spread_home

urlpatterns = [
    path('', spread_home, name='spread_home'),
]
