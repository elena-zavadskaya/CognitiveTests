from turtle import pd

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer, ResultSerializer, TestSerializer
from django.contrib.auth.hashers import make_password, check_password
import logging

import pandas as pd
from django.http import HttpResponse
from .models import AppUser, Profile, Test, Result

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
        logger.info("Полученные данные: %s", request.data)
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
        logger.error("Ошибки валидации: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultView(APIView):
    def post(self, request):
        logger.info("Полученные данные: %s", request.data)

        # Преобразуем score_percentage в число
        request.data['score_percentage'] = float(request.data.get('score_percentage', 0))

        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.error("Ошибки валидации: %s", serializer.errors)
        return Response(
            {"error": "Invalid data", "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

class TestListView(APIView):
    def get(self, request):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TestDetailView(APIView):
    def get(self, request, test_id):
        try:
            test = Test.objects.get(id=test_id)
            serializer = TestSerializer(test)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Test.DoesNotExist:
            return Response({'error': 'Тест не найден'}, status=status.HTTP_404_NOT_FOUND)


def export_users_results_excel(request):
    users = AppUser.objects.all()
    profiles = Profile.objects.all()
    results = Result.objects.all()

    data = []
    for user in users:
        profile = profiles.filter(user=user).first()
        user_results = results.filter(user=user)

        for result in user_results:
            data.append({
                'ID пользователя': user.id,
                'Никнейм': user.nickname,
                'Возраст': profile.age if profile else None,
                'Эмоциональное состояние': profile.mood if profile else None,
                'Образование': profile.education if profile else None,
                'Специальность': profile.speciality if profile else None,
                'Место жительства': profile.residence if profile else None,
                'Рост': profile.height if profile else None,
                'Вес': profile.weight if profile else None,
                'Основная рука': profile.lead_hand if profile else None,
                'Заболевания': profile.diseases if profile else None,
                'Курение': profile.smoking if profile else None,
                'Алкоголь': profile.alcohol if profile else None,
                'Спорт': profile.sport if profile else None,
                'Бессонница': profile.insomnia if profile else None,
                'Текущее состояние здоровья': profile.current_health if profile else None,
                'Игры': profile.gaming if profile else None,
                'Название теста': result.test.title if result.test else None,
                'Процент правильных ответов': result.score_percentage if result else None
            })

    df = pd.DataFrame(data)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=users_results.xlsx'

    df.to_excel(response, index=False)

    return response

