На компьютере должен быть установлен [Docker](https://www.docker.com/get-started/)

Загружаем проект.

Открываем терминал в папке проекта и вводим команду:

`docker-compose up`

Ждем пока все загрузится.

Открываем в проекте другую вкладку терминала и вводим команду:

`docker exec -it pgdb psql -U postgres`

Подключаемся к базе данных, отдаем права пользователю, прописываем хост.

` \c fastapi_database`

`grant all privileges on database fastapi_database to postgres;`

`psql -h pgdb -p 5432 postgres`

Открываем еще одну вкладку терминала и подключаемся к контейнеру fastapi

`docker exec -it fastapi bash`

Заходим в оболочку Python

`python`

Подключаем модуль services и создаем таблицу

`import services`

`services._add_tables()`

[Запускаем приложение на локальном сервере http://localhost:8000/docs](http://localhost:8000/docs)

Откроется меню с двумя запросами

1. POST /load_questions
   1. раскрываем меню
   2. Кликаем "Try it out"
   3. В параметр questions_num вводим количество вопросов для загрузки
   4. Кликаем "Exeсute"
   5. В ответе должно прийти "[INFO] Данные успешно загружены" так же может быть дополнительная информация, если в ответе были вопросы, которые уже находятся в базе данных.
2. GET /questions
   1. раскрываем меню
   2. Кликаем "Try it out"
   3. Кликаем "Exeсute" 
   4. В ответе должны прийти все вопросы, которые находятся в базе.
   5. Так же этот [запрос](http://localhost:8000/questions) можно сделать в адресной строке браузера.

Чтобы остановить приложение в первой вкладке нажимаем CTRL+С.

Чтобы запустить приложение заново в терминале вводим команду 

`docker-compose up`

