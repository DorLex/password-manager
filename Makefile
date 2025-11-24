infra:
	docker compose up -d postgres

server:
	POSTGRES_HOST=localhost python manage.py runserver

up:
	docker compose up -d --build

tests:
	POSTGRES_HOST=localhost python manage.py test -v 2
