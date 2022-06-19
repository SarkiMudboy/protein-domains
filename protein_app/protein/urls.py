from django.urls import path
from .views import *

name = 'protein'

urlpatterns = [
    path('<str:taxa_id>/', ProteinListView.as_view()),
]
