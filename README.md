# Проект Благотворительный фонд поддержки котиков QRkot_Spreadseets

Проект создан в рамках обучения <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer">FastAPI</a> на факультете Бэкенд. Когорта №9+ Яндекс.Практикум.

Использованы следующие технологии и пакеты:
<p align="left"> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"> </a>
<a href="https://www.sqlalchemy.org/" target="_blank" rel="noreferrer"> <img src="https://github.com/devicons/devicon/blob/master/icons/sqlalchemy/sqlalchemy-original.svg" alt="sqlalchemy" width="40" height="40"> </a>
<a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer"><img src="https://github.com/devicons/devicon/blob/master/icons/fastapi/fastapi-original.svg" alt="fastapi" width="40" height="40"> </a>
<a href="https://github.com/sqlalchemy/alembic" target="_blank" rel="noreferrer"><img src="https://github.com/awkward/Alembic/blob/master/Docs/icon.png" alt="alembic" width="40" height="40"> </a>
<a href="https://github.com/fastapi-users/fastapi-users" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/fastapi-users/fastapi-users/master/logo.svg" alt="fastapi-users"> </a>
</p>

<h3 align="left">Описание:</h3>

Фонд собирает пожертвования на различные целевые проекты.

Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

В Фонде может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается. Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

<h3 align="left">Отчет в Google Spreadsheets:</h3>

Отчёт формируется в гугл-таблице. В него также входят закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму. 
Для использования отчёта, необходимо подключить к проекту сервисный аккаунт Google.


<h3 align="left">Установка:</h3>

Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone 
```

```
cd QRkot_spreadsheets
```

Cоздайте и активируйте виртуальное окружение:

```
python3 -m venv venv
```

Установите pip, зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создате файл.env, запишите в него переменные:

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

Примените миграции командой:

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

<h3 align="left">Об авторе:</h3>
<a href="https://github.com/erges699" target="_blank">Сергей Баляба</a>
