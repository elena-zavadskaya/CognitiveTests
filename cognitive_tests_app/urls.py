from django.urls import path
from .views import RegisterView, LoginView, ProfileView, ResultView, TestListView, TestDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('result/', ResultView.as_view(), name='result'),
    path('tests/', TestListView.as_view(), name='test-list'),
    path('tests/<int:test_id>/', TestDetailView.as_view(), name='test-detail'),
]