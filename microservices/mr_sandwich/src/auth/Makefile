sh:
	docker exec -it microservices_mr_sandwich_auth bash

envs:
	docker exec -it microservices_mr_sandwich_auth printenv

m:
	docker exec -it microservices_mr_sandwich_auth bash cd _migrations && alembic upgrade head
