# RabbitMQ
AMQP service to process messages between services. In our case it is RabbitMQ, but amqp protocol is also supported by
other system like AWS SQS for instance.

## Hosts
| Service     | Development host                          | Compose/Swarm host                        |
|-------------|-------------------------------------------|-------------------------------------------|
| Admin Panel | [localhost:15672](http://localhost:15672) | [localhost:15672](http://localhost:15672) |