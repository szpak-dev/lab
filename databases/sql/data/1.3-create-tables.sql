CREATE TABLE IF NOT EXISTS rentals.cars (
    id serial PRIMARY KEY,
    company varchar(32) not null,
    model varchar(32) not null,
    license_plate varchar(16) not null,
    manufacture_year date not null,
    mileage integer not null
);

CREATE TABLE IF NOT EXISTS rentals.clients(
    id serial PRIMARY KEY,
    full_name varchar(64) not null,
    phone varchar(16) not null,
    registered_at date not null
);

CREATE TABLE IF NOT EXISTS rentals.rentals (
    id serial PRIMARY KEY,
    car_id integer REFERENCES rentals.cars(id) not null,
    client_id integer REFERENCES rentals.clients(id) not null,
    starts_at date not null,
    ends_at date not null,
    incident_happened boolean not null
);