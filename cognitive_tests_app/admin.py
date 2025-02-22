from django.contrib import admin
from .models import User, Profile, Test, Result


# Регистрация модели User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname')  # Отображаемые поля в списке
    search_fields = ('nickname',)  # Поля для поиска
    list_filter = ('nickname',)  # Фильтры в правой панели


# Регистрация модели Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'age', 'education', 'speciality')  # Отображаемые поля
    search_fields = ('user__nickname', 'education', 'speciality')  # Поля для поиска
    list_filter = ('education', 'speciality', 'smoking', 'gaming')  # Фильтры


# Регистрация модели Test
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')  # Отображаемые поля
    search_fields = ('title', 'description')  # Поля для поиска
    list_filter = ('title',)  # Фильтры


# Регистрация модели Result
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'test', 'score_percentage')  # Отображаемые поля
    search_fields = ('user__nickname', 'test__title')  # Поля для поиска
    list_filter = ('test__title', 'score_percentage')  # Фильтры
