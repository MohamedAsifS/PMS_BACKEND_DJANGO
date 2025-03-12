from django.urls import path 
from .views import CreatingCoordinator


urlpatterns = [
   path('coordinator',CreatingCoordinator.as_view())
]
