# posts/serializers.py
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:

        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:

        fields = ('username', 'email','password')
        model = User     

class ChangeEmailSerializer(serializers.ModelSerializer):
        class Meta:
            fields = ('email',)
            model = User     