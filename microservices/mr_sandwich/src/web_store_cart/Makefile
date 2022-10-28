venv:
	python3 -m venv venv
	source venv/bin/activate

fr:
	pip freeze > app/requirements.txt

exec:
	docker exec -it microservices_mr_sandwich_web_store_cart bash

envs:
	docker exec -it microservices_mr_sandwich_web_store_cart printenv