# 🚀 Django Application

Приложение на Django с WebSocket поддержкой, REST API и красивым интерфейсом.

## 📋 Содержание

- [Обзор проекта](#обзор-проекта)
- [Технические характеристики](#технические-характеристики)
- [Архитектура](#архитектура)
- [Установка и запуск](#установка-и-запуск)
- [API документация](#api-документация)
- [Функциональность](#функциональность)
- [Структура проекта](#структура-проекта)
- [Модели данных](#модели-данных)

## 🎯 Обзор проекта

Полнофункциональное приложение, демонстрирующее все возможности Django ORM, включая различные типы связей между моделями, REST API, WebSocket соединения для уведомлений в реальном времени и современный пользовательский интерфейс.

### ✨ Основные возможности

- 📝 **CRUD операции** для всех сущностей (посты, комментарии, теги, профили)
- 🔗 **REST API** с полной функциональностью
- ⚡ **WebSocket уведомления** в реальном времени
- 👤 **Автоматическое управление пользователями** (создание тестовых аккаунтов)
- 🐳 **Docker поддержка** для легкого развертывания

## 🛠 Технические характеристики

### Backend
- **Django 5.2.1** - веб-фреймворк
- **Django REST Framework 3.16.0** - API
- **Django Channels** - WebSocket поддержка
- **Redis** - брокер сообщений для Channels
- **SQLite** - база данных

### Frontend
- **JavaScript** - интерактивность
- **WebSocket API** для real-time обновлений

### DevOps
- **Docker & Docker Compose** - контейнеризация
- **uv** - современный менеджер пакетов Python

## 🏗 Архитектура

### Модели данных и связи

```python
User (Django встроенная)
├── Profile (OneToOne) - профиль пользователя
├── Post (ForeignKey) - посты блога
└── Comment (ForeignKey) - комментарии

Post
├── Tag (ManyToMany) - теги
├── Comment (ForeignKey) - комментарии к посту
└── User (ForeignKey) - автор

Comment
├── Post (ForeignKey) - связанный пост
└── User (ForeignKey) - автор комментария

Tag
└── Post (ManyToMany) - связанные посты
```

### API Endpoints

```
/api/posts/          - Посты (CRUD)
/api/comments/       - Комментарии (CRUD)
/api/tags/           - Теги (CRUD)
/api/profiles/       - Профили пользователей (CRUD)
/api/users/          - Пользователи (Read Only)
```

## 🚀 Установка и запуск

### Вариант 1: Docker (Рекомендуется)

```bash
# Клонировать репозиторий
git clone https://github.com/Ayturgan/testpython.git
cd testpython

# Запустить с Docker Compose
docker-compose up --build
```

Приложение будет доступно по адресу: http://localhost:8001

### Вариант 2: Локальная установка

#### Требования
- Python 3.11+
- Redis (для WebSocket)
- PostgreSQL (опционально, для продакшена)

#### Установка

```bash
# Клонировать репозиторий
git clone https://github.com/Ayturgan/testpython.git
cd testpython

# Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate     # Windows

# Установить зависимости
pip install -r requirements.txt

# Или использовать uv (рекомендуется)
pip install uv
uv sync
```

#### Настройка базы данных

По умолчанию используется **SQLite** для локальной разработки.
Для продакшена поддерживается **PostgreSQL**.

```bash
# Создать и применить миграции
python manage.py makemigrations
python manage.py migrate

# Создать суперпользователя (опционально)
python manage.py createsuperuser
```

#### Настройка PostgreSQL (опционально)

Для использования PostgreSQL установите переменные окружения:

```bash
export PGHOST=localhost
export PGDATABASE=blog_db
export PGUSER=blog_user
export PGPASSWORD=your_password
export PGPORT=5432
```

#### Запуск

```bash
# Запустить Redis (в отдельном терминале)
redis-server

# Запустить Django сервер
python manage.py runserver 0.0.0.0:8000
```

## 📚 API документация

### Автоматическая документация

- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/

### Основные endpoints

#### Посты
```http
GET    /api/posts/           # Список всех постов
POST   /api/posts/           # Создать новый пост
GET    /api/posts/{id}/      # Получить конкретный пост
PUT    /api/posts/{id}/      # Обновить пост
DELETE /api/posts/{id}/      # Удалить пост
```

#### Комментарии
```http
GET    /api/comments/        # Список всех комментариев
POST   /api/comments/        # Создать новый комментарий
GET    /api/comments/{id}/   # Получить конкретный комментарий
PUT    /api/comments/{id}/   # Обновить комментарий
DELETE /api/comments/{id}/   # Удалить комментарий
```

#### Пример создания поста
```json
POST /api/posts/
{
    "title": "Мой первый пост",
    "content": "Содержание поста..."
}
```

**Примечание**: Автор назначается автоматически из списка тестовых пользователей.

## 🎮 Функциональность

### Веб-интерфейс

Доступен по адресу: http://localhost:8001/app/

#### Возможности интерфейса:

1. **📝 Управление постами**
   - Создание новых постов
   - Просмотр списка постов
   - Детальный просмотр в модальных окнах
   - ✏️ **Редактирование постов** (inline формы)
   - 🗑️ **Удаление постов** (с подтверждением)

2. **💬 Комментарии**
   - Просмотр комментариев к постам
   - Добавление новых комментариев
   - ✏️ **Редактирование комментариев** (inline формы)
   - 🗑️ **Удаление комментариев** (с подтверждением)

3. **🏷 Теги**
   - Создание и управление тегами
   - Связывание тегов с постами
   - ✏️ **Редактирование названий тегов**
   - 🗑️ **Удаление тегов** (с предупреждением об удалении из постов)

4. **👤 Профили пользователей**
   - Просмотр профилей
   - Отображение статистики пользователей

5. **📊 Статистика в реальном времени**
   - Количество постов, комментариев, пользователей
   - Автоматическое обновление через WebSocket

**✨ Все CRUD операции реализованы:**
- ✅ **CREATE** - формы создания для всех сущностей
- ✅ **READ** - просмотр списков и детальная информация  
- ✅ **UPDATE** - inline редактирование с сохранением
- ✅ **DELETE** - удаление с подтверждением

### Административная панель

Доступна по адресу: http://localhost:8000/admin/

- Полное управление всеми сущностями
- Расширенная админка с кастомными настройками
- Фильтрация и поиск

## 📁 Структура проекта

```
TestPython/
├── app/                    # Главное приложение
│   ├── models.py          # Модели данных
│   ├── views.py           # API views
│   ├── serializers.py     # DRF сериализаторы
│   ├── admin.py           # Конфигурация админки
│   ├── urls.py            # URL маршруты
│   ├── consumers.py       # WebSocket consumers
│   ├── routing.py         # WebSocket routing
│   └── signals.py         # Django сигналы
├── core/                  # Настройки проекта
│   ├── settings.py        # Главные настройки
│   ├── urls.py            # Главные URL
│   ├── asgi.py            # ASGI конфигурация
│   └── wsgi.py            # WSGI конфигурация
├── templates/             # HTML шаблоны
│   └── app_interface.html # Главный интерфейс
├── docker-compose.yml     # Docker Compose конфигурация
├── Dockerfile            # Docker образ
├── pyproject.toml        # Зависимости проекта
└── README.md             # Документация
```

## 🗃 Модели данных

### User (встроенная Django модель)
- Стандартная модель пользователя Django
- Связана с Profile через OneToOne

### Profile
```python
class Profile:
    user = OneToOneField(User)      # Связь с пользователем
    bio = TextField()               # Описание
    location = CharField()          # Местоположение
```

### Post
```python
class Post:
    title = CharField(200)          # Заголовок
    content = TextField()           # Содержание
    author = ForeignKey(User)       # Автор
    tags = ManyToManyField(Tag)     # Теги
    created_at = DateTimeField()    # Дата создания
    updated_at = DateTimeField()    # Дата обновления
```

### Comment
```python
class Comment:
    post = ForeignKey(Post)         # Связанный пост
    author = ForeignKey(User)       # Автор комментария
    text = TextField()              # Текст комментария
    created_at = DateTimeField()    # Дата создания
```

### Tag
```python
class Tag:
    name = CharField(50, unique=True)  # Название тега
```


### Настройки Docker

В `docker-compose.yml` уже настроены:
- Django приложение (порт 8000)
- Redis (порт 6379)
- Автоматические перезапуски
- Синхронизация кода

## 🧪 Тестирование

### Автоматические тестовые данные

Приложение автоматически создает тестовых пользователей:
- Alice Johnson (alice_blogger)
- Bob Smith (bob_writer)  
- Carol Brown (carol_author)
- David Wilson (david_commenter)
- Eva Davis (eva_reader)

### Тестирование API

```bash
# Получить все посты
curl http://localhost:8000/api/posts/

# Создать новый пост
curl -X POST http://localhost:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Post", "content": "Test content"}'

# Получить пост по ID
curl http://localhost:8000/api/posts/1/
```

## 📄 Лицензия

MIT License - см. файл LICENSE для деталей.

**🎉 Приложение готово к использованию! Наслаждайтесь современным Django приложением!**
