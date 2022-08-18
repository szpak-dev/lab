# Running SQL Scripts (Lesson: Database, Schemas and Tables)
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

## Using app
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