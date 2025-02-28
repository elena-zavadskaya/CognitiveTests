from rest_framework import serializers
from .models import AppUser, Profile, Result, Test


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

class ResultSerializer(serializers.ModelSerializer):
    test = serializers.PrimaryKeyRelatedField(queryset=Test.objects.all())  # Используем PrimaryKeyRelatedField
    user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all())

    class Meta:
        model = Result
        fields = ['test', 'user', 'score_percentage']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'title', 'description']