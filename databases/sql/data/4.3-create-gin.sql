CREATE INDEX client_names_gin_index ON rentals.clients USING GIN (full_name);