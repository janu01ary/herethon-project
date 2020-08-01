from django.urls import path
from . import views
from hereapp import views

urlpatterns = [
    path('new/', views.new, name='new'),

    
]