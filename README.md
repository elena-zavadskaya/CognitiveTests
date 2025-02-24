# Название проекта

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/elena-zavadskaya/CognitiveTests.git
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv .venv
   ```

3. Активируйте виртуальное окружение:
   - На Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - На macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

5. Примените миграции:
   ```bash
   python manage.py migrate
   ```

6. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```

7. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

8. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/`.
