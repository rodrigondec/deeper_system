################################################################################
# Docker-compose pyramid service commands for dev
################################################################################

run:
	docker-compose run pyramid $(cmd)

flake8:
	docker-compose run pyramid flake8

migrate:
	docker-compose run pyramid python manage.py migrate $(app)

makemigrations:
	docker-compose run pyramid python manage.py makemigrations

test:
	docker-compose run pyramid pytest --disable-warnings -v

bash:
	docker-compose run pyramid bash

shell:
	docker-compose run pyramid python manage.py shell

coverage:
	docker-compose run pyramid coverage run --source='.' manage.py test $(app)
	docker-compose run pyramid coverage report

up:
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

build:
	docker-compose build

install:
	docker-compose run pyramid pip install -e ".[testing]"

remove.volumes:
	docker-compose down
	docker volume rm deeper_system_postgres_data

clear.python:
	find . -type d -name __pycache__ -o \( -type f -name '*.py[co]' \) -print0 | xargs -0 rm -rf

clear.docker:
	docker ps | awk '{print $$1}' | grep -v CONTAINER | xargs docker stop
