from django.urls import path

from . import views

urlpatterns = [
    path("registrations/", views.ResgitrationListView.as_view()),
    path("registrations/<str:pk>/", views.RegistrationCreateView.as_view()),
    path("registrations/detail/<str:pk>/", views.RegistrationDetailView.as_view()),
]
