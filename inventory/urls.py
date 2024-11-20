from django.urls import path
from . import views

urlpatterns = [
    path('scan-barcode/', views.scan_barcode, name='scan_barcode'),
    path('drug-list/', views.drug_list, name='drug_list'),
]
