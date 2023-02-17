# Welcome To The Microservices Tutorial Lab
Learning new technologies shouldn't go without some good practice, that's why I'm giving you a fully configured and
production-ready system, which will help you better understand Microservices-related concepts.

## Ingredients
As you can see, there are two directories in the root of this tutorial: `specification`, which contains all necessary
documentation, and `src` containing Microservices. This is supposed to be your main workspace, every topic mentioned
in the articles being part of [Microservices](https://www.szpak.dev/tutorials#microservices) tutorial on the 
**[Information Technology by Tomasz Szpak](https://www.szpak.dev/)** blog.

## What Is Inside?
This project resides within **monolithic repository** (monorepo). All microservices are being kept and managed from the
top of `src` directory. Next to directories containing applications' sources, there are two files, which will help
you run, build and test whole stack of services (not only micro). Let's take a closer look what lays deeper.

* [specification](specification)
  * contains global constraints and agreements
  * tells about decisions behind architectural choices using **Architecture Decision Record**
  * provides a visual diagram of system architecture with **C4 Model**
* [src](src)
  * contains Python3 web apps, which run in containers
  * organizes containers locally with docker-compose
  * provides Makefile for dev environment

## What If Something Goes Wrong?
If you have any problems with running the system, just create an Issue and describe your problem. I will do my best to 
answer you as soon as possible.