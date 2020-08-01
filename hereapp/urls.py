from django.urls import path
from . import views
from hereapp import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('addemail/', views.addemail, name='addemail'),
    path('mypage/', views.mypage, name="mypage"),
    path('showresults/', views.showresults, name='showreulsts'),
]