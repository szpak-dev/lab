rb:
	docker-compose build --no-cache $(s) && \
	docker-compose up -d $(s) && \
	docker-compose logs --follow $(s)

rbauth:
	@make rb s=auth

rbauthw:
	@make rb s=auth_worker

rbfoodfactory:
	@make rb s=food_factory

rbfoodfactoryw:
	@make rb s=food_factory_worker

rbloadbalancer:
	@make rb s=load_balancer

rbwebstorecart:
	@make rb s=web_store_cart

ps:
	docker-compose ps

im:
	docker-compose images

l:
	docker-compose logs --follow $(s)

rr:
	docker-compose up -d $(s)
	@make l $(s)