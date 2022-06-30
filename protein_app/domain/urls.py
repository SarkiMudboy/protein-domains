from django.urls import path
from .views import *

name = 'pfam'

urlpatterns = [
    path('get-domain/<int:id>', DomainView.as_view()),
    path('domain', DomainListView.as_view()),
    path('update/<str:domain_id', DomainView.as_view()),
    path('delete/<str:domain_id', DomainView.as_view()),
    path('', PfamListView.as_view()),
    path('<str:domain_id>/', PfamView.as_view()),
    path('get-pfam/<str:taxa_id>', PfamTaxaListView.as_view()),
    path('update/<str:domain_id>', PfamView.as_view()),
    path('delete/<str:domain_id>', PfamView.as_view())
]