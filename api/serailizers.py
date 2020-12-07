from rest_framework import serializers
from signUp.models import user_details


# Signin Serializer
class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = ('user_name', 'email', 'password')
    
    def retrive(self,validated_data):
        data = user_details.objects

# Signup Serializer
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = ('user_name', 'email', 'password')

    def create(self, validated_data:tuple):
        """validated_data should contain (user_name,email,password)"""
        user = user_details.objects.create(user_name=validated_data[0], email=validated_data[1], password=validated_data[2])
        return user