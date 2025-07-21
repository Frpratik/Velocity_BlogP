from rest_framework import serializers
from .models import Blog, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    commenter_username = serializers.ReadOnlyField(source='commenter.username')

    class Meta:
        model = Comment
        fields = '__all__'

#==========================================================================================

class BlogSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

#==========================================================================================

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
#==========================================================================================