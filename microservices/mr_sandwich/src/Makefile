rb:
	docker-compose build --no-cache $(s) && \
	docker-compose up -d $(s) && \
	docker-compose logs --follow $(s)

rba:
	@make s=auth

rbaw:
	@make s=auth_worker

rbf:
	@make s=food_factory

rbfw:
	@make s=food_factory_worker

rbl:
	@make s=load_balancer

ps:
	docker-compose ps

im:
	docker-compose images

l:
	docker-compose logs --follow

ll:
	docker-compose logs --follow $(s)

rall:
	docker-compose restart && docker-compose logs --follow

r:
	docker-compose up -d $(s)
	@make ll $(s)