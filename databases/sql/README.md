# SQL Database Lab (PostgreSQL 14.4)
Hello and welcome to the lab. To connect with the cluster run this command:

```shell
docker exec -it postgres psql postgres postgres
```

You are now connected with PostgreSQL. Now let's see what command are available.

## Commands
First, let's find out something about the connection:

```shell
\conninfo
```
You should see this:

`You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".`

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

## Running SQL Scripts
If you take a look at the `*.sql` scripts inside `data` directory, you will notice they are prefixed with numbers. Each
number corresponds to article ordinal and query ordinal inside post. To fulfill first part of the tutorial, please run 
first four scripts. How?

```shell
\i /opt/scripts/1.1-create-database.sql
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
\i /opt/scripts/1.2-create-schema.sql
```

To confirm that schema was created, you can run:

```shell
\dn
```

If `rentals` is listed together with `public` we are good to go and create tables:

```sql
\i /opt/scripts/1.3-create-tables.sql
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

## Feed the Tables
Empty tables are useless, so according to the second article in the tutorial, we will now create list of our assets - 
the cars. All necessary **INSERT**s are here:

```sql
\i /opt/scripts/2.1-insert-cars.sql
```