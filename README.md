# Task API

REST API для задач на Django REST Framework (Task, Category, Tag).

## Запуск

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Или через Docker: `docker compose up --build`

## Эндпоинты

- `GET, POST /api/v1/tasks/`: список, создание
- `GET, PUT, PATCH, DELETE /api/v1/tasks/{id}/`: детали, обновление, удаление

`category` и `tags` передаются как id существующих объектов (создаются в админке `/admin/`).