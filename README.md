# Laboratory (szpak.dev)
Welcome to the **Lab**, which is a practical side of tutorials ar articles available on 
[Information Technology by Tomasz Szpak](https://www.szpak.dev) blog and learning center. Let's get to work.

# What Is Inside?
**Lab** is a project, which contains another projects inside, depending on their categories. They live inside directories,
which are named using the pattern:

```shell
<main_category>/<some_id>
```

Let's take a tour of available projects:

* [databases/sql](databases/sql):
  * provides pre-configured PostgreSQL container
  * scripted with all examples presented in the [tutorial](https://www.szpak.dev/tutorials/#databases-sql)
  * comes with some convenient commands and application
  * can be pre-loaded with dummy data
* [domain-driven-design/tactical](domain-driven-design/tactical):
  * classes and files from Domain-Driven Design tactical part of tutorial
  * presents building blocks of tactical ddd
  * uses python for example code
  * introduces SOLID principles
* [microservices/mr_sandwich](microservices/mr_sandwich):
  * production ready microservices packed in to a monorepo
  * fabularized content from very beginning of the project to its final deployment
  * blueprints in form of **C4 Model**, **Open Api Standard** and **Architecture Decision Records**
  * whole architecture is configured and ready to be extended

To help you read the code together with the README files, they are spread across the directories and placed next to the
topic they are referring to.

# Prerequisites
In order to run the **Lab**, you are going to need a few things first:

* Computer with Linux, MacOS or [Windows with Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install)
* [Docker](https://docs.docker.com/get-docker/) in the newest version available
* [make](https://www.gnu.org/software/make/) tool to execute [Makefile](https://opensource.com/article/18/8/what-how-makefile),
which is used to conveniently run necessary commands on both `containers` and `localhost`
* some IDE like [PyCharm](https://www.jetbrains.com/pycharm/) or [VS Code](https://code.visualstudio.com/docs/languages/python) 
for your convenience