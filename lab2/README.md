## Что разворачивает docker-compose
- `db`: PostgreSQL 16-alpine, хранилище в томе `postgres_data`, healthcheck через `pg_isready`.
- `migrate`: одноразовый контейнер, выполняет `alembic upgrade head` после того как БД стала healthy.
- `app`: FastAPI/Uvicorn, порты `8000:8000`, healthcheck через `curl -f http://localhost:8000/hello`.

## Переменные окружения (.env)
Ожидаются переменные для подключения к БД (см. `.env`), например:
```
POSTGRES_USER=test
POSTGRES_PASSWORD=test
POSTGRES_DB=test_db
```
Файл `.env` не коммитится, но лежит рядом с `docker-compose.yml`.

## Как запустить
- Собрать и запустить все сервисы: `docker compose up --build`
- Проверить API: `curl http://localhost:8000/hello`

## Ответы на вопросы
- Ограничение ресурсов: в Docker Compose ресурсы задают через секцию `deploy.resources.limits|reservations`
- Запуск одного сервиса: `docker compose up app` (или другое имя) поднимет только его;