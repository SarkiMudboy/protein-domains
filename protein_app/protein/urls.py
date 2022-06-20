from django.urls import path
from .views import *

name = 'protein'

urlpatterns = [
    path('<str:taxa_id>/', ProteinListView.as_view()),
    path('', ProteinListView.as_view()),
    path('get/<str:protein_id>/', ProteinRetrieveView.as_view()),
]
