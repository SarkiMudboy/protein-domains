from django.urls import path
from .views import *

app_name = 'pfam'

urlpatterns = [
    path('get-domain/<int:id>', DomainView.as_view(), name='get-domain'),
    path('domain', DomainListView.as_view(), name='domain'),
    path('domain/update/<str:domain_id', DomainView.as_view(), name='update-domain'),
    path('domain/delete/<str:domain_id', DomainView.as_view(), name='delete-domain'),
    path('', PfamListView.as_view(), name='pfam-list'),
    path('<str:domain_id>/', PfamView.as_view(), name='get-pfam-domain'),
    path('get-pfam/<str:taxa_id>', PfamTaxaListView.as_view(), name='get-pfam-taxa'),
    path('update/<str:domain_id>', PfamView.as_view(), name='pfam-update'),
    path('delete/<str:domain_id>', PfamView.as_view(), name='pfam-delete')
]