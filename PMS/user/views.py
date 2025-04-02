from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from  rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
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
class GetUser(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    
    def get(self, request, *args, **kwargs):
        user=request.user
        return Response({'iscoordinator':user.is_coordinator,"department":user.department,"year":user.year})
    