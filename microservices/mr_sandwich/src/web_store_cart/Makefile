sh:
	docker exec -it microservices_mr_sandwich_web_store_cart bash

envs:
	docker exec -it microservices_mr_sandwich_web_store_cart printenv

dev:
	uvicorn main:app --reload --port 8002

mm:
	alembic revision --autogenerate -m "${m}"