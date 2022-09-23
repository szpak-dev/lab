from pypika import Table, PostgreSQLQuery as Query
import db.connector as db_connector

connection = db_connector.connection(no_transaction=False)
cursor = db_connector.cursor()

columns_map = {
    'clients': ('full_name', 'phone', 'registered_at'),
}


def create_client_row():
    return (
        faker.name(),
        faker.phone_number(),
        faker.date(),
    )


def insert_clients(num):
    insert_batch(num, 'clients', create_client_row)


def insert_batch(num, table_name, row):
    table = Table(table_name)
    query = Query.into(table)

    num += 1
    batch = []

    for n in range(1, num):
        batch.append(row())
        if num % 100 == 0:
            insert_exec(query, batch, columns_map[table_name])

        if (n + 1) == num and len(batch) > 0:
            insert_exec(query, batch, columns_map[table_name])


def insert_exec(query, batch, columns_list):
    q = query.columns(columns_list).insert(*batch)

    cursor.execute(str(q))
    connection.commit()






