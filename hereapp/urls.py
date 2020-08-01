from django.urls import path
from . import views

urlpatterns = [
    path('addemail/', views.addemail, name='addemail'),
    path('mypage/', views.mypage, name="mypage"),
    path('showresults/', views.showresults, name='showreulsts')
]