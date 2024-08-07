# Описание проекта «API для Yatube»
Проект API для социальной сети Yatube

# Установка
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

# Примеры запросов к API
GET запрос, список всех постов:
```
/api/v1/posts/
```
POST запрос, список всех постов:
```
/api/v1/posts/
```
GET запрос, детальная информация о посте:
```
/api/v1/posts/{post_id}/
```
POST запрос, заменить пост:
```
/api/v1/posts/{post_id}/
```
PATCH запрос, обновить пост:
```
/api/v1/posts/{post_id}/
```
DELETE запрос, удалить пост:
```
/api/v1/posts/{post_id}/
```
