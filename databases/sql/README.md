# SQL Database Lab (PostgreSQL 14.4)
Hello and welcome to the Database SQL lab. You should treat this as a **hands-on** experience when going through
**Databses (SQL)** tutorial available on [Information Technology](https://szpak.dev/tutorials#sql)

# Before You Start
This Laboratory was made with a [Docker](https://www.docker.com/get-started/), great tool for containerizing 
applications. In this case there are two apps included:

* **PostgreSQL** - version 14.4
* **db_sql** - application written especially for this tutorial in Python, to make everything easier for you

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
All work will be done on the `db_sql` container. It has already all required libraries and software, so you don't have 
to worry about installing them. The interesting fact is, that many people just quit learning because they cannot
manage how to install and configure additional software. To connect with `db_sql`:

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

If you did this, reconnect, so we can continue with creating our tables.

# Running SQL Scripts (Lesson: Database, Schemas and Table)
If you take a look at the `*.sql` scripts inside `/opt/data` directory, you will notice they are prefixed with numbers. 
Each number corresponds to article ordinal and query ordinal inside post. To fulfill first part of the tutorial, please 
run first four scripts. How?

```shell
\i /opt/data/1.1-create-database.sql
```

SQL files are very convenient way to run long queries, which would be cumbersome to type and run. Run `\l` to see if 
there is our new database. If all went well, there should be a `car_rentals` listed. Good, now we will create a schema.
Please remember, that you don't have to run files like we've just did - you can copy-paste their contents and run in 
psql client.

Since you are still connected to `postgres` database (creating a new one doesn't automagically switch to it), what you 
have to do is to reconnect to our target:

```shell
\c car_rentals
```

When successful, you should see the following message: `You are now connected to database "car_rentals" as user "postgres".`
Great success. Now, we can create our schemas:

```sql
\i /opt/data/1.2-create-schema.sql
```

To confirm that schema was created, you can run:

```shell
\dn
```

If `rentals` is listed together with `public` we are good to go and create tables:

```sql
\i /opt/data/1.3-create-tables.sql
```

To check if tables were created, run:

```shell
\dt rentals.*
```

or suffix command with a plus sign `+` to get even more information:

```shell
\dt+ rentals.*
```

Mind the asterisk here: `*`. Since `dt` is mnemonic of **d**escribe **t**able, you have to use a wildcard to get details
about all the tables in the **schema**. To print a particular table's info, you need to type:

```shell
\dt rentals.cars
\dt+ rentals.cars
```

## Using db_sql
There is a bunch of handy scripts which allow you to perform mentioned tasks with just single command. To use them, you 
have to leave a postgres context first.

```shell
# create database, schema and tables
db_sql --init

# insert data from all examples used in tutorial
db_sql --data

# drop and create tables to start all over
db_sql --reset

# add n fake clients records to rentals.clients table
db_sql --clients=200

# add n random cars records to rentals.cars table
db_sql --cars=100
```

# Feed the Tables (Lesson: Create, Read, Update, Delete)
Empty tables are useless, so according to the second article in the tutorial, we will now create list of our assets - 
the cars. All necessary **INSERT**s are here:

```sql
\i /opt/data/2.1-insert-cars.sql
```

You can now practice all examples from the lesson.

# Joining (Lesson: Joins)
In order to insert Cars and rentals, you have to run these SQL scripts:

```sql
\i /opt/data/3.1-insert-clients.sql
\i /opt/data/3.2-insert-rentals.sql
```

You can now proceed to having fun with SQL queries. Please, remember that examples used in the tutorial are just a tiny
fraction of what you can do with the data. Don't hesitate to try other ways to fetch or manipulate the data.

# Indexing Data In Tables (Lesson: Indexes)
When it comes to huge amounts of data, a properly **indexed** tables are crucial for overall system efficiency. You can 
use the fastest programming language out there, but it's all in vain when the data source becomes a bottleneck. Before
you start creating indexes, do some experiment first. Using **db_sql**, insert a significant numbers of records to one
of the tables (clients or cars) and try to select some rows using **WHERE** clause. Observe how much time will it take
for a Postgres to return a result. Then, index a column which was used in a query you've run and observe how much faster
it gets. Remember, that all necessary SQL commands are there in **data** directory. Also, in case of any problems, you 
can always start a new Issue in the Lab repository. Good luck.

