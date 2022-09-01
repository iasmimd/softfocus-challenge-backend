from django.urls import path

from analysts import views

urlpatterns = [
    path("analysts/", views.AnalystView.as_view()),
]