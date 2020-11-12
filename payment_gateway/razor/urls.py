from django.urls import path, include
from .views import home, confirm
urlpatterns = [
   
    path('', home, name='home'),
    path('confirm', confirm, name='confirm'),
]
