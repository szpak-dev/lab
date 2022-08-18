# SQL Database Lab (PostgreSQL 14.4)
Hello and welcome to the Database SQL lab. You should treat this as a **hands-on** experience when going through
**Databases (SQL)** tutorial available on [Information Technology](https://szpak.dev/tutorials#sql)

# Before You Start
This Laboratory was made with a [Docker](https://www.docker.com/get-started/), great tool for containerizing 
applications. In this case there are two apps included:

* **PostgreSQL** - version 14.4
* **app** - application written especially for this tutorial in Python, to make everything easier for you

If you have questions, doubts or don't know what to do, then create an Issue in this repository.

# Installing the Lab
If you have docker installed, then you are ready to go. First, we have to build and start our containers. Before we go,
just take a look at `docker-compose.yml` file, there you can find definitions of services which are part of your 
practice. And after you do this, open the terminal and simply type:

```shell
docker-compose up -d
```

This command will build and start all containers, and because we have used a `-d` argument, after it finishes the 
initiating process, it will go to the background. We are now ready to continue.

# Starting the Lab
All work will be done on the `databases_sql_app` container. It has already all required libraries and software, so you 
don't have to worry about installing them. The interesting fact is, that many people just quit learning because they 
cannot manage how to install and configure additional software. To connect with `databases_sql_app`:

```shell
./connect.sh
```

If all went well, you should now see a prompt inside a container:

```shell
/opt # 
```

Whenever you want to stop the connection, simply type:

```shell
exit
```

and it will take you back to your host machine.

# Talking Straight To Database
Great, you did very well. Being here, we can now connect with PostgreSQL 14.4 using a special client program called 
`psql`. To save you some searching there is a special command available, which using `psql` and connects with a cluster.
Simply type:

```shell
postgres
```

And you are now connected with PostgreSQL what looks like this:

```shell
psql (14.4)
Type "help" for help.

postgres=#
```

You can always type `exit` command to end working with PostgreSQL cluster. Now let's see what commands are available.

## Basic PostgreSQL Commands With Psql
First, let's find out something about the connection:

```shell
\conninfo
```
You should see this:

`You are connected to database "postgres" as user "postgres" on host "postgres" (address "172.18.0.3") at port "5432".`

If not, you probably did something wrong. Please follow the instructions and try once again. The message you've just 
seen tells a lot - you are connected to the default database named `postgres` and the user, which is also a default one,
is `postgres`.

Now, let's list all databases which are present in current cluster:

```shell
\l
```

As you can see, there is aforementioned `postgres` database and two templates. To list all the tables, sequences and 
other objects in the database run:

```shell
\z
```

What you should see at this moment is an empty table with headers only. So far, so good. To quit current session type:

```shell
\q
```

If you did this, reconnect, so we can continue to the next lessons.

# Lessons
You know how to use the Lab, so we can now proceed to the lessons.

* [Database, Schemas and Tables](docs/database-schemas-table.md)
* [Create, Read, Update, Delete](docs/crud.md)
* [Joins](docs/joins.md)
* [Index Types](docs/index-types.md)
* [Transactions](docs/transactions.md)