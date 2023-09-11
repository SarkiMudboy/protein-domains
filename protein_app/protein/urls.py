from django.urls import path
from .views import *

app_name = 'protein'

urlpatterns = [
    path('<str:taxa_id>/', ProteinListView.as_view(), name='protein-list'),
    path('', ProteinListView.as_view(), name='protein-create'),
    path('get/<str:protein_id>/', ProteinView.as_view(), name='protein-get'),
    path('update/<str:protein_id>/', ProteinView.as_view(), name='protein-update'),
    path('delete/<str:protein_id>/', ProteinView.as_view(), name='protein-delete'),
    path('taxa/get/<str:taxa_id>/', TaxaView.as_view(), name='taxa-get'),
    path('taxa', TaxaCreateView.as_view(), name='taxa-create'),
    path('taxa/update/<str:taxa_id', TaxaView.as_view(), name='taxa-update'),
    path('taxa/delete/<str:taxa_id', TaxaView.as_view(), name='taxa=delete'),
]
