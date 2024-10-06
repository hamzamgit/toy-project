.PHONY: build up ssh server down flake8 test

build:
	docker-compose build

up:
	docker-compose up -d

ssh:
	docker exec -it blogapp /bin/bash

server:
	docker exec -it blogapp python manage.py runserver 0.0.0.0:8000

down:
	docker-compose down

flake8:
	docker exec -it blogapp flake8 .

test:
	docker exec -it blogapp python manage.py test
