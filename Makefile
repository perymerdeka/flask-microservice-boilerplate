build:
	docker compose build --no-cache

up:
	docker-compose up

upd:
	docker-compose up -d

shell:
	docker-compose exec web-api bash

db-init:
	docker-compose exec web-api su -c "flask db init"

db-upgrade:
	docker-compose exec web-api su -c "flask db upgrade"

db-migrate:
	docker-compose exec web-api su -c "flask db migrate"


destroy:
	docker-compose down -v

deploy-dev:
	make build && make up

deploy:
	make build && make upd


# production mode
build-prod:
	docker-compose -f docker-compose-prod.yaml build --no-cache

up-prod:
	docker-compose -f docker-compose-prod.yaml up

upd-prod:
	docker-compose -f docker-compose-prod.yaml up -d

deploy-prod-dev:
	make build-prod && make up-prod

deploy-prod:
	make build-prod && make upd-prod

shell-prod:
	docker-compose -f docker-compose-prod.yaml exec web-api bash

db-upgrade-prod:
	docker-compose -f docker-compose-prod.yaml exec web-api su -c "flask db upgrade"

db-init-prod:
	docker-compose -f docker-compose-prod.yaml exec web-api su -c "flask db init"

db-migrate-prod:
	docker-compose -f docker-compose-prod.yaml exec web-api su -c "flask db migrate"