# 🚂 Развертывание на Railway

## Изменения для Railway Deploy

### ✅ Исправлена проблема со стилями админки и Swagger

**Проблема:** При использовании Gunicorn/Unicorn стили админки Django и Swagger UI не загружались (оставался только HTML без CSS/JS).

**Причина:** Gunicorn и другие WSGI/ASGI серверы не обслуживают статические файлы автоматически, в отличие от встроенного сервера разработки Django (`runserver`).

**Решение:** 
- Заменили Gunicorn на встроенный `runserver` Django
- Включили `DEBUG=True` для корректной обработки статических файлов
- Добавили сбор статических файлов через `collectstatic`

### 🔧 Настройки Railway

**Файл `railway.json`:**
```json
{
  "deploy": {
    "startCommand": "sh -c 'python manage.py collectstatic --noinput && python manage.py migrate && python manage.py create_superuser_if_not_exists && python manage.py runserver 0.0.0.0:$PORT'"
  }
}
```

**Последовательность команд:**
1. `collectstatic --noinput` - собираем статические файлы
2. `migrate` - применяем миграции БД  
3. `create_superuser_if_not_exists` - создаем админа (если не существует)
4. `runserver 0.0.0.0:$PORT` - запускаем сервер разработки

### 👤 Автоматическое создание суперпользователя

Создана кастомная команда Django: `app/management/commands/create_superuser_if_not_exists.py`

**Параметры:**
- **Логин:** `admin`  
- **Email:** `admin@example.com`
- **Пароль:** `qwerty123`

Команда создает суперпользователя только если он не существует, предотвращая ошибки при повторных запусках.

### 🔧 Настройки Django для Railway

**`core/settings.py`:**
- `DEBUG = True` для Railway (необходимо для `runserver`)
- Поддержка PostgreSQL через переменные окружения Railway
- Настройка Redis для WebSocket (если доступен)
- Правильная конфигурация `STATIC_ROOT` и `STATIC_URL`

**`core/urls.py`:**
- Добавлена обработка статических файлов в режиме разработки
- `static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)`

### 🌐 Railway Services

В `railway.json` настроены 3 сервиса:
- **web** - Django приложение
- **postgresql** - База данных  
- **redis** - Для WebSocket уведомлений

### 🚀 Доступ к приложению

После развертывания на Railway:
- **Главная страница:** `https://your-app.railway.app/app/`
- **Админка Django:** `https://your-app.railway.app/admin/` (admin/qwerty123)
- **Swagger API:** `https://your-app.railway.app/swagger/`
- **API Endpoints:** `https://your-app.railway.app/app/api/`

### ⚠️ Важные замечания

1. **Режим разработки:** Используется `DEBUG=True` и `runserver` - подходит для тестирования, не для продакшена
2. **Статические файлы:** Обслуживаются встроенным сервером Django
3. **Безопасность:** Для продакшена нужно настроить nginx + gunicorn + whitenoise
4. **Производительность:** `runserver` не предназначен для высоких нагрузок

### 🔄 Для продакшена

Если нужен продакшен-деплой, рекомендуется:
- Использовать Gunicorn + WhiteNoise для статических файлов
- Настроить nginx как reverse proxy
- Отключить DEBUG
- Настроить правильные ALLOWED_HOSTS 