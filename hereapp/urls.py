from django.urls import path
from . import views
from hereapp import views

urlpatterns = [
    path('addemail/', views.addemail, name='addemail'),
    path('mypage/', views.mypage, name="mypage"),
    path('showresults/', views.showresults, name='showreulsts'),
    path('sendallresults/', views.sendallresults, name='sendallresults'),
    path('ok/', views.okpage, name="okpage"),
    path('deleteemail/<int:pk>', views.deleteemail, name='deleteemail'),
]