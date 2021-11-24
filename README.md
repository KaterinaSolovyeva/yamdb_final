![YaMDB workflow](https://github.com/KaterinaSolovyeva/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# Описание.

Проект "YaMDb" собирает отзывы пользователей на различные произведения.

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/nu-shtosh/api_yamdb
```
```
cd api_yambd
```
Создайте файл .env командой touch .env. Шаблон наполнения env-файла:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```
```
Запустите docker-compose командой sudo docker-compose up -d
```
Создайте миграции: 
```
docker-compose exec web python manage.py makemigrations --noinput
docker-compose exec web python manage.py migrate --noinput
```
Соберите статику проекта командой:
```
sudo docker-compose exec web python manage.py collectstatic --no-input
```
Создайте суперпользователя Django:
```
sudo docker-compose exec web python manage.py createsuperuser
```
Загрузите тестовые данные в базу данных командой: 
```
sudo docker -compose exec web python manage.py loaddata fixtures.json
```
# Примеры запросов к API.

Получение списка всех произведений
```
GET /api/v1/titles/
```
Получить список всех отзывов к определенному произведению по его id
```
GET /api/v1/titles/{title_id}/reviews/
```
Получить список всех комментариев к отзыву по id
```
GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```



Writers:

https://github.com/KaterinaSolovyeva

https://github.com/nu-shtosh

https://github.com/Xewus
