# Mr. Sandwich Services
Welcome to the Microservices tutorial. Since we are 
[Domain-Driven Design](https://www.szpak.dev/blog/microservices/introduction/why-microservices) practitioners, our 
services will be split by the [Bounded Contexts](https://www.szpak.dev/blog/domain-driven-design/strategic/bounded-context).
We have found three of them:

* **food_factory** 
  * is a monolith-like system, 
  * uses Django because of its Admin Panel, which gives CRUD almost for free
* **web_store**
  * split into three real microservices:
    * cart
    * payment
    * invoice
  * uses fully-blown `Onion` (layered) architecture
* **delivery**
  * responsible for delivering order to the customer
  * provides a backend and logic for deliverer's mobile application

Every Bounded Context has one or more `Aggregate` inside. Aggregates communicate using `Domain Event` as a carrier.

## Application Layout Pattern
Every microservice defined in this project follows a certain pattern when it comes to laying out the files. Let me show 
you how it's done. What we have here is a bunch of [12 Factor Apps](https://12factor.net/) (12App), which have some 
common tools and shortcuts:

* **app** (directory)
  * contains source files of the given service
  * root directory, its content is copied into container under `/opt/app` directory
  * stores frozen pip dependencies
* **venv** (directory, not in vcs)
  * keeps virtualenv files
  * ignored by the vcs
* _api_docs.yaml_
  * endpoints documented with Open Api Standard (Swagger)
  * can be used to generate client code for other services
* _Dockerfile_
  * definition how to build a container
  * configured with environmental variables only, it allows updating a container without rebuild (12App)
  * env vars are overwritten by those from `docker-compose.yml` file or from Systems Manager in [aws](aws.com)
* _worker.Dockerfile_
  * responsible for building worker container
  * also configured via env vars
* _Makefile_
  * convenient targets
  * frequently used commands

## Architectures Per Microservice
Microservices use different architectures and frameworks, so you can choose what fits best for your project. Let's  go
quickly through the most significant aspects of every service.

### Load Balancer
Microservice named [load_balancer](load_balancer) acts like a gateway and proxies requests to the proper service. 
Internally it uses a [Caddy](https://caddyserver.com/) server, which provides 
[ssl](https://www.cloudflare.com/learning/ssl/what-is-ssl/) and easy configuration syntax out-of-the-box.

### Auth
[auth](auth) is a service, which handles request's authorization and passing it to the proper microservice. It uses 
architecture called `Ports and Adapters` and [Flask](https://palletsprojects.com/p/flask/), which handles HTTP requests.

### Food Factory
To manage production and dishes, there is a service called [food_factory](food_factory). It doesn't use any specialized
architecture, because it deals mostly with [CRUD](https://www.szpak.dev/blog/databases/sql/crud) operations. Backed by
the [Django](https://www.djangoproject.com/) framework.

### Web Store Cart
Microservice called [web_store_cart](web_store_cart) is very small and specialized one, because it only deals with a 
Shopping Cart functionality. Presents Saga pattern.