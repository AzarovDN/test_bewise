
`docker-compose run fastapi`

`docker-compose down`

`docker-compose up`

Открываем в проекте другую вкладку терминала

`docker exec -it pgdb psql -U postgres`

Подключаемся к базе данных
` \c fastapi_database`

`grant all privileges on database fastapi_database to postgres;`

`psql -h pgdb -p 5432 postgres`

Открывакем еще одну вкладку терминала и подключаемся к контейнеру fastapi

`docker exec -it fastapi bash`

Заходим в оболочку Python
`python`

Подключаем модуль servces и создаем таблицу

`import services`

`services._add_tables()`

[Запускаем приложение на локальном сервере http://localhost:8000/docs](http://localhost:8000/docs)


