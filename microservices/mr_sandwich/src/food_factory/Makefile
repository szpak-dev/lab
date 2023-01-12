envs:
	docker exec -it microservices_mr_sandwich_food_factory printenv

sh:
	docker exec -it microservices_mr_sandwich_food_factory bash

dbexec:
	docker exec -it --user postgres microservices_mr_sandwich_food_factory_db psql

dbmm:
	python manage.py makemigrations

dbmr:
	python manage.py migrate

dev:
	python manage.py runserver 8100
