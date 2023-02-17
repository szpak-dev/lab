# Mr. Sandwich Microservices
Welcome to the Microservices tutorial. Since we are 
[Domain-Driven Design](https://www.szpak.dev/blog/microservices/introduction/why-microservices) practitioners, our 
services will be split by the [Bounded Contexts](https://www.szpak.dev/blog/domain-driven-design/strategic/bounded-context).
Let me describe them briefly.

## Running The Stack
Everything is configured and waiting to be built. To start the stack, simply run:

```shell
docker-compose up -d
```

Reverse Proxy service is configured with a default domain, which is `mr.localhost`, so don't forget to edit your 
`hosts` file by appending this line:

```
127.0.0.1 mr.localhost
```

After few minutes everything will be installed and ready to work. Send request to `https://mr.localhost/auth/login` and
if you can see a response, then everything is fine.

## Naming Conventions For Services
Every Microservice has an ecosystem of surrounding containerized applications: web application, one or more workers
and independent database. Naming convention is as follows:

* <service_name>
  * manages REST API and HTTP in general
* <service_name>**_worker**
  * infinitely running process
  * AMQP consumer in most cases
* <service_name>**_db**
  * database dedicated to the service
  * independent from other databases

## Business Microservices
First category of services are those which handles business logic behind a particular Bounded Context.

### [Auth](auth)
[API-Gateway](https://www.ibm.com/cloud/blog/api-gateway) responsible for authentication, which uses 
**Ports And Adapters** architecture.

### [Food Factory](food_factory)
Service for handling food production and Dishes together with their Reservations.

### [Web Store Cart](web_store_cart)
Cart functionality for Web Store. Implemented with an **Onion (Layered)** architecture.

## Infrastructure And Monitoring Services
Second category of services handles infrastructure and monitoring-related issues.

### [Reverse Proxy](reverse_proxy)
This service reverse proxying HTTP requests with [Caddy Server](https://caddyserver.com/).

### [RabbitMQ](rabbitmq)
Service implementing [amqp](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol) protocol.

### [Prometheus](prometheus)
[Time-series database](https://prometheus.io/) for metrics collecting.
