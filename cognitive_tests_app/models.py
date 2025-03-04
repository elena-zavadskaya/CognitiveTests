from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class AppUser(models.Model):
    nickname = models.CharField(max_length=50, unique=True, verbose_name="Никнейм")
    password_hash = models.CharField(max_length=255, verbose_name="Хэш пароля")

    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['nickname']

class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="profile"
    )
    age = models.SmallIntegerField(null=True, blank=True, verbose_name="Возраст")
    mood = models.SmallIntegerField(null=True, blank=True, verbose_name="Эмоциональное состояние")  # Новое поле
    education = models.CharField(max_length=255, null=True, blank=True, verbose_name="Образование")
    speciality = models.CharField(max_length=255, null=True, blank=True, verbose_name="Специальность")
    residence = models.CharField(max_length=255, null=True, blank=True, verbose_name="Место жительства")
    height = models.SmallIntegerField(null=True, blank=True, verbose_name="Рост")
    weight = models.SmallIntegerField(null=True, blank=True, verbose_name="Вес")
    lead_hand = models.CharField(max_length=255, null=True, blank=True, verbose_name="Основная рука")
    diseases = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заболевания")
    smoking = models.BooleanField(null=True, blank=True, verbose_name="Курение")
    alcohol = models.CharField(max_length=255, null=True, blank=True, verbose_name="Алкоголь")
    sport = models.CharField(max_length=255, null=True, blank=True, verbose_name="Спорт")
    insomnia = models.BooleanField(null=True, blank=True, verbose_name="Бессонница")
    current_health = models.SmallIntegerField(null=True, blank=True, verbose_name="Текущее состояние здоровья")
    gaming = models.BooleanField(null=True, blank=True, verbose_name="Игры")

    def __str__(self):
        return f"Профиль пользователя {self.user.nickname}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ['user__nickname']

class Test(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Название теста")
    description = models.TextField(verbose_name="Описание теста")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        ordering = ['title']

class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    score_percentage = models.IntegerField(verbose_name="Процент правильных ответов")
    # Старое название ↓↓↓          Новое название ↓↓↓
    time = models.CharField(max_length=20, verbose_name="Время выполнения теста")  # Было time_spent
    number_all_answers = models.PositiveIntegerField(verbose_name="Количество вопросов")  # Было total_questions
    number_correct_answers = models.PositiveIntegerField(verbose_name="Правильных ответов")  # Было correct_answers

    def __str__(self):
        return f"Результат пользователя {self.user.nickname} в тесте {self.test.title}: {self.score_percentage}%"

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"
        ordering = ['-score_percentage']