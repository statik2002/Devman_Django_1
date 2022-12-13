# Сайт интерактивной карты Москвы для активного досуга

## Общее описание
Сайт написан на фреймворке Django в учебных целях по уроку №1 по фреймворку Django.

Пример рабочего сайта представлен по адресу [https://statik2002.pythonanywhere.com/](https://statik2002.pythonanywhere.com/)


## Установка
Установить виртуальное окружение, например командой:
```commandline
python3 -m venv env
```

Войти в виртуальное окружение командой:
```commandline
source env/bin/activate
```

Установить зависимости командой:
```commandline
pip install -r requirements.txt
```

Создать файл `.env` в корневой папке сайта и внести туда следующие данные:
1. `SECRET_KEY`= 'секретный ключ'
2. `DEBUG`= При продакшене ставим `False`
3. `ALLOWED_HOSTS`='127.0.0.1,IP сервера'
4. `DB_ENGINE`='драйвер БД' например 'django.db.backends.sqlite3'
5. `DB_NAME`='Имя БД' например 'db.sqlite3'
6. `DB_HOST`: 'Адрес БД',
7. `DB_USER`='Имя пользователя БД'
8. `DB_PASSWORD`='Пароль к БД'
9. `DB_PORT`='Порт БД'

Выполнить миграции командой:
```commandline
python manage.py migrate
```

Собрать статику командой:
```commandline
python manage.py collectstatic
```

Создать суперпользователя командой:
```commandline
python manage.py createsuperuser
```

## Запуск
Запуск сервера производиться командой:
```commandline
python manage.py runserver
```