venv:
	python3 -m venv venv
	source venv/bin/activate

dev:
	python app/manage.py runserver

pi:
	pip install $(s)

pui:
	pip uninstall $(s)

fr:
	pip freeze > app/requirements.txt

sh:
	docker exec -it microservices_mr_sandwich_food_factory bash

dbexec:
	docker exec -it --user postgres microservices_mr_sandwich_food_factory_db psql

dbmm:
	python app/manage.py makemigrations

dbmr:
	python app/manage.py migrate

envs:
	docker exec -it microservices_mr_sandwich_food_factory printenv