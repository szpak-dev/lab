venv:
	python3 -m venv venv
	source venv/bin/activate

pi:
	pip install $(s)

pui:
	pip uninstall $(s)

fr:
	pip freeze > app/requirements.txt

exec:
	docker exec -it microservices_mr_sandwich_auth bash

envs:
	docker exec -it microservices_mr_sandwich_auth printenv
