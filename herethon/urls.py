from django.contrib import admin
from django.urls import path, include
import hereapp.views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),git 
    path('', hereapp.views.index,name='home'),
    path('here/', include('hereapp.urls')),
    path('accounts/', include('accounts.urls'))
]
