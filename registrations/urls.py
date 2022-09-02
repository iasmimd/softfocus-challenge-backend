from django.urls import path

from . import views

urlpatterns = [
    path('registrations/<str:pk>/', views.RegistrationView.as_view()),
    path('registrations/detail/<str:pk>/', views.RegistrationDetailView.as_view()),
]