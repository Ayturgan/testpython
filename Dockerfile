FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1     

WORKDIR /app

RUN pip install --no-cache-dir pip-tools

COPY pyproject.toml .

RUN pip install --no-cache-dir -e .

COPY . .

EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "core.asgi:application"]
