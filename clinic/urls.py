
from django.contrib import admin
from django.urls import path, include
#from django.db import models


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls'))
]
