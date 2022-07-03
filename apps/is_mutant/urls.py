"""is_mutant app urls."""

# Django
from django.urls import path

# Vistas
from apps.is_mutant import views

urlpatterns = [
    path('mutant/', views.IsMutant.as_view(), name="is_mutant"),
    path('stats/', views.Stats.as_view(), name="stats")
]