from django.urls import path
from .views import *

name = 'protein'

urlpatterns = [
    path('<str:taxa_id>/', ProteinListView.as_view()),
    path('', ProteinListView.as_view()),
    path('get/<str:protein_id>/', ProteinView.as_view()),
    path('update/<str:protein_id>/', ProteinView.as_view()),
    path('delete/<str:protein_id>/', ProteinView.as_view()),
    path('taxa/get/<str:taxa_id>/', TaxaView.as_view()),
    path('taxa', TaxaCreateView.as_view()),
    path('taxa/update/<str:taxa_id', TaxaView.as_view()),
    path('taxa/delete/<str:taxa_id', TaxaView.as_view()),
]
