from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import UserSerializer
from .models import User

# Create your views here.
class CreatingCoordinator(CreateAPIView):
    """
    this CBV is used to create the placment cordinator from the Placment cell staff
    """
    queryset = User.objects.all()
    serializer_class=UserSerializer
    
    def perform_create(self, serializer):
        serializer.save(is_coordinator=True,is_staff=True)
        