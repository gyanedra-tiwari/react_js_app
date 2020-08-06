from .models.accounts import User
from .models.accounts import Profile
from taggit.models import Tag
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
import json


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'   

    def validate_password(self, value: str) -> str:
        return make_password(value)   

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'   
  
                
class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:

        model = Profile
        fields = ['first_name', 'last_name', 'username', 'user']

    def get_username(self, obj):
        user = obj.user.username
        return user





