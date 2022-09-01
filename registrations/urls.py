from django.urls import path

from . import views

urlpatterns = [
    path('registrations/<int:pk>/', views.RegistrationView.as_view()),
]