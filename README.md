# QRkot_spreadseets
<h1 align="center">Привет! </h1>
<h3 align="center">Я студент факультета Бэкенд. Когорта №9+ Яндекс.Практикум</h3>
<h3 align="center"><a href="https://github.com/erges699" target="_blank">Сергей Баляба</a></h3>
<h3 align="center">Разрабатываю проект <a href="https://github.com/erges699/git@github.com:erges699/QRkot_spreadsheets.git" target="_blank">API-сервис: Благотворительный фонд поддержки котиков</a></h3>
<h3 align="left">В настоящее время изучаю <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer">FastAPI</a>, в проекте использую следующие библиотеки: </h3>

- 🔭 Python
- 🔭 SQLAlchemy
- 🔭 FastAPI
- 🔭 FastAPIUsers (JWT tokens)
- 🔭 Alembic


<h3 align="center">Проект Благотворительный фонд поддержки котиков. Описание:</h3>

Фонд собирает пожертвования на различные целевые проекты.

В Фонде может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается. Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd QRkot_spreadsheets
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

Установить pip, зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать файл.env, записать в него:

```
APP_TITLE=Благотворительный фонд поддержки котиков
APP_DESCRIPTION=Описание проекта 
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=Секретный ключ
FIRST_SUPERUSER_EMAIL=email суперпользователя, создается при первом запуске
FIRST_SUPERUSER_PASSWORD=пароль суперпользователя, создается при первом запуске
TYPE=service_account
PROJECT_ID=some project id
PRIVATE_KEY_ID=SomePrivate key Id
PRIVATE_KEY=private key
CLIENT_EMAIL=client email
CLIENT_ID=client id
AUTH_URI=данные для авторизации в google api
TOKEN_URI=данные для авторизации в google api
AUTH_PROVIDER_X509_CERT_URL=данные для авторизации в google api
CLIENT_X509_CERT_URL=данные для авторизации в google api
EMAIL=эл.почта google аккаунта пользователя, имеющего доступ к отчету
```

Применить миграции командой:

```
alembic upgrade head
```

Запуск проекта:

```
uvicorn app.main:app --reload
```

При первом запуске будет создан суперпользователь, если в файле .env были заполнены переменные FIRST_SUPERUSER_EMAIL и FIRST_SUPERUSER_PASSWORD

Документация API по адресу:

```
http://127.0.0.1:8000/docs
```
