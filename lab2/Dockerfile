FROM ghcr.io/astral-sh/uv:python3.11-alpine

LABEL description="DOCKERFILE FOR LAB 2"

WORKDIR /app


RUN apk add --no-cache curl
RUN adduser --gecos '' --disabled-password appuser

COPY pyproject.toml .
RUN uv sync --no-cache-dir

COPY alembic.ini .
COPY migrations/ migrations/

COPY app/ .

USER appuser

EXPOSE 8000

CMD ["uv", "run", "python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]