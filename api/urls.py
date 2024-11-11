from django.urls import path
from .views import post_data_transfer

urlpatterns = [
    path('data_transfer/', post_data_transfer, name='pdata_transfer')
]