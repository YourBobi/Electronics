## Диаграмма таблиц 

https://drawsql.app/teams/my-team-1021/diagrams/electronics

## Команды
docker-compose build
docker-compose up
docker-compose run --rm electronics-app sh -c "python manage.py makemigrations"
docker-compose run --rm electronics-app sh -c "python manage.py migrate"
docker-compose run --rm electronics-app sh -c "python manage.py createsuperuser"