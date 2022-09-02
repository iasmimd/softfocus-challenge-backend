from django.urls import path

from analysts import views

urlpatterns = [
    path("analysts/", views.AnalystView.as_view()),
    path("login/", views.CustomAuthToken.as_view()),
]