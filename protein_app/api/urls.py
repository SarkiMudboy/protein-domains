from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import RegisterView, ResearcherView, AuthTokenView

app_name = 'researchers'

urlpatterns = [
    path('login/', AuthTokenView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='auth_register'),

    path('researchers/<int:pk>', ResearcherView.as_view(), name='researcher'),
]