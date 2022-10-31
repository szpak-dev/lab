# Authentication Bounded Context
This is our first Bounded Context. For microservices, there maybe a little too many responsibilities, but we have 
decided to make a split of our Monolith to Microservices using Bounded Contexts, so here we are. Authentication is not
strictly a business rule, but it fits into a Domain as a feature list required for recognizing users.

## Architecture
Architecture used for the software, is called `Ports and Adapters`. In this philosophy of code organization, **Ports** 
are what **Domain** expect from the remaining blocks of code, which are **User Interface** and **Infrastructure**. By 
defining a Port, the Domain tells how it will be driven and/or how it will drive the provided **Adapters**. Please mind,
that Ports belong to the business logic, that's why they live in `domain` directory, defined as **Interfaces**.

What is important here, is that we use an Inversion of Control (IoC), so Adapters are loaded by their abstraction 
(interface) instead of concrete implementation. It abstracts out how data is provided, and focuses on the data itself.
It works on both, driving and driven ports. It encourages you to define three building blocks in your code:

* **User Interface**
  * a piece of code, a real or machine user interacts with
  * may be anything from http request to cli command
  * driven by **Driving Adapters** based on Port interface like http, cli, etc.
* **Business Logic**
  * also called **Application Core**
  * place where all business rules are defined and checked for validity
  * here happens actual orchestration of checks and calculations
  * drives **Driven Adapters**, mostly external services like database, api, etc.
* **Infrastructure**
  * code responsible for implementing interfaces of **Driven Adapters**
  * driven by Business Logic

We will dive into Aggregates and their Ports And Adapters soon, but first let me explain the structure of the root 
folder.

## Root Files And Directories
If you take a closer look on the files and directories, this is what you will see:
* **app**
  * contains two Aggregates: `Session` and `User`
  * Aggregates use Event Bus build on Mediator pattern to communicate
  * there are some DDD common components like `Repository`, `AggregateRoot` or `DomainEvent`

The remaining files are described in the Lab's README.md file.

## Aggregates
As already said, Authentication (Auth in short) Bounded Context contains two Aggregates: User and Session. Every 
Aggregate includes two directories: `domain` and `adapters`, which are mandatory minimum. Let's see what they consist:

* `domain/ports`: 
  * list of **Ports** defined as interfaces (abstract classes)
  * concrete implementations reside in the `adapter` folder, outside scope of Domain
  
* `domain/entities`: 
  * **DDD** building block, usually full of behaviours, so each one has its own file
  * module contains factory function to build given entity
  
* `domain/value_objects.py`: 
  * another **DDD** building block
  * when number becomes significant, then split to files and put into directory with the same name

* `domain/services`: 
  * **DDD** services, 
  * they are responsible for validating **business rules**
  * they don't rely on adapters

* `domain/errors.py`: 
  * taxonomy of Domain Events, 
  * main error must inherit directly from `DomainEvent`
  * the rest of errors must directly inherit from `<AggregateName>Error`

* `adapters/__init__.py`: 
  * a heart and soul of **Adapters**
  * responsible for building and exporting adapter implementation, based on its interface
  * naming convention is `<prefix>_<port_name>`: 
    * `in_memory_jwt_repository`
    * `redis_session_repository`

Since we know what is the structure of the Aggregate, let's go through **User** and **Session**, and see what are their 
responsibilities.

### User
This Aggregate is built around `User`. The **Entity** handles password checking, but that's all for now. Let's take a 
look for the Ports:

* `domain/ports/api_service.py`: 
  * provides currently logged in User
* `domain/ports/credentials_checker.py`:
  * checks if username and password match, if no throws exception
* `domain/ports/user_creator.py`:
  * creates new User
* `domain/ports/user_repository.py`:
  * fetches User by username
  * saves User
* `domain/ports/user_transceiver.py`:
  * transmitter and receiver of User-related Events
  * emits event, when credentials were confirmed, used during login process
  * listening when authentication starts, so it can check if given user and password match

### Session
Built around `Session`, which doesn't do much. But what are the ports?

* `domain/ports/api_service.py`:
  * handles login and logout
  * provides current username
* `domain/ports/jwt_repository.py`:
  * responsible for creating and validating JWT
* `domain/ports/request_interceptor.py`:
  * api gateway pattern
  * everything what is not `auth` will be passed to the dedicated service inside private network
* `domain/ports/session_repository.py`:
  * manages sessions
  * provides usernames
* `domain/ports/session_transceiver.py`:
  * transmitter and receiver of Session-related Events
  * emits Event, when Authentication starts
  * listen for confirmed credentials from User Aggregate

## Summary
In this service, I have used **Ports And Adapters** architecture. It gave us a holy grail of a good software project:
**loose coupling** and **high cohesion**. User and Session does not rely on each other anywhere, they are totally 
independent. They only place containing tight coupling is the `Flask` factory method where controllers live. Mediator
components do not use object but primitive values, so they can be kept separated.
