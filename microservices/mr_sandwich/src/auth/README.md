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
* .dockeignore
  * keeps your local venv directory out of production build
* .env
  * sets names for docker-compose, thanks to this you have nicely formatted service names in log
  * keeps some instance-specific values, they need to be reflected in your cloud environment like AWS -> Systems Manager
* .gitignore
  * all build and cache-related artifacts should stay on your local machine
  * you can modify it as you need
* connect.sh
  * convenient way to enter app container
* Dockerfile
  * contains build instructions for a container
  * uses specific python version, so there is no need for `virtual_env`
  * defining entrypoint in a separated file gives us change to run some operations when service starts
* entrypoint.sh
  * responsible for running flask application
  * may orchestrate some additional tasks when service starts
* requirements.txt
  * freezed pip packages
  * every package is locked on exact semver, so no surprises when new production build is deployed
* venv.sh
  * handy script for local development
  * activates `virtual_env`

## Aggregates
As it was already said, Authentication (Auth in short) Bounded Context contains two Aggregates: User and Session.
Let me explain what happens in the code.

### User Aggregate
