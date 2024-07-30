from rest_framework import viewsets
from .models import Blog
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = UserSerializer
