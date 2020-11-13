from django.urls import path, include
from .views import home, confirm, pay
urlpatterns = [
   
    path('', home, name='home'),
    path('status', confirm, name='status'),
    path('pay', pay, name = 'pay'),
]
