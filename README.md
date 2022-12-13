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

## Как загрузить локации в БД

Для загрузки новых локаций необходимо воспользоваться командой `load_place`

Запуск осуществляется следующим образом:

```commandline
python manage.py load_place [url]
```

Где [url] - ссылка на файл json с локацией.

Для примера вид json файла:

```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```