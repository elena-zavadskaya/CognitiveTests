from django.contrib import admin
from django.urls import path
from django.urls import reverse
from django.utils.html import format_html
from .models import AppUser, Profile, Test, Result
from .views import export_users_results_excel  # Функция экспорта

class AppUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname')
    search_fields = ('nickname',)
    list_filter = ('nickname',)
    change_list_template = "admin/appuser_changelist.html"

    def get_urls(self):
        """Добавляем кастомный URL для экспорта"""
        urls = super().get_urls()
        custom_urls = [
            path('export/', self.admin_site.admin_view(self.export_users_results), name='export_users_results'),
        ]
        return custom_urls + urls

    def export_users_results(self, request):
        """Вызывает функцию экспорта"""
        return export_users_results_excel(request)

admin.site.register(AppUser, AppUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'education', 'speciality')
    search_fields = ('user__nickname', 'education', 'speciality')
    list_filter = ('education', 'speciality', 'smoking', 'gaming')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'test',
        'score_percentage',
        'time',
        'number_all_answers',
        'number_correct_answers'
    )
    search_fields = ('user__nickname', 'test__title')
    list_filter = (
        'test__title',
        'score_percentage',
        'number_all_answers'
    )
