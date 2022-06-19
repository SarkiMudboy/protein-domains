from django.urls import path
from .views import *

name = 'pfam'

urlpatterns = [
    path('', PfamListView.as_view()),
    path('<str:domain_id>/', PfamRetrieveView.as_view()),
]