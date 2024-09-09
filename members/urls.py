from django.urls import path
from . import views

urlpatterns = [
    path('', views.members_data, name='members_data'),
]