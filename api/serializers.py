from rest_framework import serializers
from .models import Blog

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['url', 'username', 'email', 'is_staff']
