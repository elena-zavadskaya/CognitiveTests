from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from cognitive_tests_app.views import export_users_results_excel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cognitive_tests_app.urls')),
    path('export_users_results/', export_users_results_excel, name='export_users_results'),
    path('', TemplateView.as_view(template_name='index.html')),
]
