from rest_framework import serializers
from .models import AppUser, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'nickname', 'password_hash']
        extra_kwargs = {'password_hash': {'write_only': True}}

    def create(self, validated_data):
        user = AppUser.objects.create(
            nickname=validated_data['nickname'],
            password_hash=validated_data['password_hash']
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all())

    class Meta:
        model = Profile
        fields = '__all__'