################################################################################
# Docker-compose pyramid service commands for dev
################################################################################

run:
	docker-compose run pyramid $(cmd)

test:
	docker-compose run pyramid pytest --disable-warnings -v

bash:
	docker-compose run pyramid bash

up:
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

build:
	docker-compose build

config.egg:
	docker-compose run pyramid pip install -e ".[testing]"

config.mongo_user:
	docker-compose run mongo mongo --host mongo -u mongo -p mongo --eval 'db = db.getSiblingDB("mongo");db.createUser({user: "mongo", pwd: "mongo", roles: [{"role": "readWrite", "db": "mongo"}]})'

config: config.egg config.mongo_user

remove.volumes:
	docker-compose down
	docker volume rm deeper_system_mongo_data

clear.python:
	find . -type d -name __pycache__ -o \( -type f -name '*.py[co]' \) -print0 | xargs -0 rm -rf

clear.docker:
	docker ps | awk '{print $$1}' | grep -v CONTAINER | xargs docker stop
