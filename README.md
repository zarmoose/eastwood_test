# База сотрудников компании

Интерфейс программы делится на пользовательскую и административную части.

В пользовательской части реализованы:
- фильтрация списка сотрудников по отделам компании с возможностью оставить в показе только людей, работающих в компании по настоящее время
- представление списка сотрудников в виде алфавитного глоссария
- показ детальной информации о выбранном сотруднике:
    - ФИО
    - дата рождения
    - e-mail
    - телефон
    - начало работы
    - окончание работы
    - должность
    - отдел

В административной части представлены:
- разделы добавления/удаления/редактирования карточек сотрудников и отделов компании
- фильтрация списка сотрудников по отделам


## Развёртывание программы
Для развёртывания программы необходим выделенный сервер под управлением ОС Ubuntu 18.04 LTS.

1. На сервере установить следующие пакеты:
- *python3-dev*
- *python3-setuptools*
- *libpq-dev*
- *postgresql*
- *postgresql-contrib*
- *nginx*
- *python3-pip*
- *virtualenv*
- *supervisor*
- *git*

2. Создать виртуальное окружение для данного проекта.
В виртуальном окружении установить пакеты:
- *django*
- *psycopg2-binary*
- *django-bootstrap4*
- *django-phone-field*
- *gunicorn* 

3. С помощью git получить исходные дексты проекта с GitHub.

4. Создать БД приложения и пользователя для работы с ней:
```
CREATE DATABASE eastwood_test;
CREATE USER eastwood_test_user WITH PASSWORD '12345';
ALTER ROLE eastwood_test_user SET client_encoding TO 'utf8';
ALTER ROLE eastwood_test_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE eastwood_test_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE eastwood_test TO eastwood_test_user;
```

5. Выполнить миграцию БД и создать суперпользователя.

6. Загрузить начальные данные в БД из файла *inital_data.json*.

7. В файле *settings.py* указать адрес сервера в параметре *ALLOWED_HOSTS* и прописать путь к статическим файлам в параметре *STATIC_ROOT*. Собрать статику в указанном каталоге (*manage.py collectstatic*).

8. Настроить веб-сервер Nginx и supervisor для обеспечения бесперебойной работы сайта.
