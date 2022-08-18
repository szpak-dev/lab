# Transactions (Lesson: Transactions)
In this lab, I'll show you how PostgreSQL implements Transactions. First, we need to create our test database, schema 
and tables. If you are not connected to app container, run:

```shell
./connect.sh
```

Now make connection via `psql` to the Postgres cluster:

```shell
postgres
```

To install database, run script:

```sql
\i /opt/data/5.1-create-database.sql
```

Now, to get into this particular database context, connect to it:

```sql
\c user_trans;
```

Great, the last step of the setup is to create schema and tables:

```sql
\i /opt/data/5.2-create.sql
```

Good, everything is ready to work. First, we will try something what makes Transaction to fail. What we'll do, is to try
insert rank with a too long name to the profiles table. Please mind, that it will be a second unit of this Transaction.

```sql
\i /opt/data/5.3-failure.sql
```

The result should be identical to this one:

```shell
BEGIN
INSERT 0 1
psql:/opt/data/5.3-failure.sql:4: ERROR:  value too long for type character varying(8)
ROLLBACK
```

First clause which is **BEGIN** starts the transaction block. Second line contains formation about **INSERT** query - 
in this case one out of two statements were successful. Third line contains an error message, it says exactly what we
expected. The last line says, that all changes were rolled-back. You can check this by running **SELECT** query:

```sql
\i /opt/data/5.5-select.sql
```

The result should be as follows:

```shell
 user_id | username | password | rank | email
---------+----------+----------+------+-------
(0 rows)
```

We now know how Transactions protect our data, so now we can add a valid data. Run:

```sql
\i /opt/data/5.4-success.sql
```

The result of this action looks like this:

```shell
BEGIN
INSERT 0 1
INSERT 0 1
COMMIT
```

Once again we have a beginning of transaction, then confirmation of two **INSERT** queries, and in the last row you can 
see a **COMMIT** clause. This is a clear sign that transaction was successful. Run **SELECT** once again:

```sql
\i /opt/data/5.5-select.sql
```

This time you should see a table with one row:

```shell
 user_id | username | password | rank |       email
---------+----------+----------+------+-------------------
       2 | username | p4ssw0rd | RANK | email@example.com
(1 row)
```

Take a look at the user_id value, this is equal 2, but we have only added one user. It happened so, because during our 
first attempt of adding both user and its profile, sequence was queried and its counter was incremented by one.

To clear everything and start all over again, switch to any other database, and run cleaning script:

```sql
\c postgres
\i /opt/data/5.6-clean-up.sql
```