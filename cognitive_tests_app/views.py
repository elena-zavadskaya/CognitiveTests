from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AppUser, Profile
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.hashers import make_password, check_password
import logging

logger = logging.getLogger(__name__)

class RegisterView(APIView):
    def post(self, request):
        logger.info("Полученные данные при регистрации: %s", request.data)
        nickname = request.data.get('nickname')
        password = request.data.get('password')

        if not nickname or not password:
            return Response({'error': 'Необходимо указать никнейм и пароль'}, status=status.HTTP_400_BAD_REQUEST)

        hashed_password = make_password(password)
        logger.info("Хэшированный пароль: %s", hashed_password)

        user = AppUser.objects.create(nickname=nickname, password_hash=hashed_password)
        return Response({'message': 'Пользователь успешно зарегистрирован', 'user_id': user.id}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        nickname = request.data.get('nickname')
        password = request.data.get('password')

        if not nickname or not password:
            return Response({'error': 'Необходимо указать никнейм и пароль'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = AppUser.objects.get(nickname=nickname)
        except AppUser.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

        if check_password(password, user.password_hash):
            return Response({'message': 'Успешный вход', 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Неверный пароль'}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    def post(self, request):
        logger.info("Полученные данные: %s", request.data)  # Логируем данные
        user_id = request.data.get('user')
        if not user_id:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            profile = Profile.objects.get(user_id=user_id)
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
        except Profile.DoesNotExist:
            serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error("Ошибки валидации: %s", serializer.errors)  # Логируем ошибки
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)