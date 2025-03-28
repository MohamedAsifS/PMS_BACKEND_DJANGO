from django.urls import path 
from .views import CreatingCoordinator,GetUser


urlpatterns = [
   path('coordinator',CreatingCoordinator.as_view()),
   path('status',GetUser.as_view())
]
