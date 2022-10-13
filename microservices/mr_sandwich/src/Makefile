rba:
	docker-compose build --no-cache auth && \
	docker-compose up -d auth && \
	docker-compose logs --follow auth

rbf:
	docker-compose build --no-cache food_factory && \
	docker-compose up -d food_factory && \
	docker-compose logs --follow food_factory

rbl:
	docker-compose build --no-cache load_balancer && \
	docker-compose up -d load_balancer && \
	docker-compose logs --follow load_balancer

ps:
	docker-compose ps

im:
	docker-compose images

l:
	docker-compose logs --follow

r:
	docker-compose restart && docker-compose logs --follow
