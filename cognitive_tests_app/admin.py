from django.contrib import admin
from .models import AppUser, Profile, Test, Result

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname')
    search_fields = ('nickname',)
    list_filter = ('nickname',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'education', 'speciality')  # Убрали 'id'
    search_fields = ('user__nickname', 'education', 'speciality')
    list_filter = ('education', 'speciality', 'smoking', 'gaming')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'test', 'score_percentage')
    search_fields = ('user__nickname', 'test__title')
    list_filter = ('test__title', 'score_percentage')
