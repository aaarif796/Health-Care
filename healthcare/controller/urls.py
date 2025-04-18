from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RegisterView, PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView, MappingListCreateView
)


urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    
    path('patients/', PatientListCreateView.as_view()),
    path('patients/<int:pk>/', PatientDetailView.as_view()),
    
    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),
    
    path('mappings/', MappingListCreateView.as_view()),
]