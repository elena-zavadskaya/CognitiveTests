from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils.timezone import now


class User(models.Model):
    """
    Модель пользователя.
    Хранит информацию о пользователе: никнейм и хэшированный пароль.
    """
    nickname = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Никнейм",
        help_text="Уникальный идентификатор пользователя"
    )
    password_hash = models.CharField(
        max_length=255,
        verbose_name="Хэш пароля",
        help_text="Хэшированный пароль пользователя"
    )

    def set_password(self, raw_password):
        """
        Устанавливает хэшированный пароль для пользователя.
        """
        self.password_hash = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """
        Проверяет, соответствует ли переданный пароль хэшированному паролю пользователя.
        """
        return check_password(raw_password, self.password_hash)

    def __str__(self):
        """
        Возвращает строковое представление пользователя (никнейм).
        """
        return self.nickname

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Profile(models.Model):
    """
    Модель профиля пользователя.
    Хранит дополнительную информацию о пользователе, такую как возраст, образование, здоровье и т.д.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Пользователь",
        help_text="Связанный пользователь"
    )
    age = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Возраст",
        help_text="Возраст пользователя"
    )
    education = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Образование",
        help_text="Уровень образования пользователя"
    )
    speciality = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Специальность",
        help_text="Профессия или специальность пользователя"
    )
    residence = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Место жительства",
        help_text="Город или страна проживания пользователя"
    )
    height = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Рост",
        help_text="Рост пользователя в сантиметрах"
    )
    weight = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Вес",
        help_text="Вес пользователя в килограммах"
    )
    lead_hand = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Основная рука",
        help_text="Основная рука пользователя (правша/левша)"
    )
    diseases = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Заболевания",
        help_text="Наличие заболеваний у пользователя"
    )
    smoking = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Курение",
        help_text="Курит ли пользователь"
    )
    alcohol = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Алкоголь",
        help_text="Употребление алкоголя пользователем"
    )
    sport = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Спорт",
        help_text="Занятия спортом пользователя"
    )
    insomnia = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Бессонница",
        help_text="Страдает ли пользователь бессонницей"
    )
    current_health = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Текущее состояние здоровья",
        help_text="Самооценка здоровья пользователя (по шкале от 1 до 10)"
    )
    gaming = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Игры",
        help_text="Увлекается ли пользователь видеоиграми"
    )

    def __str__(self):
        """
        Возвращает строковое представление профиля (никнейм пользователя).
        """
        return f"Профиль пользователя {self.user.nickname}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Test(models.Model):
    """
    Модель теста.
    Хранит информацию о тесте: название и описание.
    """
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название теста",
        help_text="Название когнитивного теста"
    )
    description = models.TextField(
        verbose_name="Описание теста",
        help_text="Подробное описание теста"
    )

    def __str__(self):
        """
        Возвращает строковое представление теста (название).
        """
        return self.title

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Result(models.Model):
    """
    Модель результата теста.
    Хранит информацию о результатах прохождения теста пользователем.
    """
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name="Тест",
        help_text="Связанный тест"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Пользователь, прошедший тест"
    )
    score_percentage = models.IntegerField(
        verbose_name="Процент правильных ответов",
        help_text="Процент правильных ответов пользователя в тесте"
    )

    def __str__(self):
        """
        Возвращает строковое представление результата (никнейм пользователя и процент правильных ответов).
        """
        return f"Результат пользователя {self.user.nickname} в тесте {self.test.title}: {self.score_percentage}%"

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"