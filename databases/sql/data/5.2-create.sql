CREATE SCHEMA IF NOT EXISTS trans;

CREATE TABLE IF NOT EXISTS trans.users (
    id serial PRIMARY KEY,
    username varchar(64) not null,
    password varchar(255) not null
);

CREATE TABLE IF NOT EXISTS trans.user_profiles (
    id serial PRIMARY KEY,
    user_id integer REFERENCES trans.users(id) not null,
    rank varchar(8) not null,
    email varchar(255) not null
);
