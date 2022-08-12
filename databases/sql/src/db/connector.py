from psycopg2.pool import ThreadedConnectionPool


def spawn():
    conn = ThreadedConnectionPool(
        minconn=1,
        maxconn=5,
        user="postgres",
        password="postgres",
        database="car_rentals",
        host="postgres",
        port=5432,
        options="-c search_path=dbo,public,rentals"
    )

    return conn.getconn()


connection_transaction = spawn()
connection_transaction_cursor = connection_transaction.cursor()

connection_no_transaction = spawn()
connection_no_transaction.autocommit = 'Off'
connection_no_transaction_cursor = connection_no_transaction.cursor()


def connection(no_transaction=False):
    if no_transaction:
        return connection_no_transaction
    return connection_transaction


def cursor(no_transaction=False):
    if no_transaction:
        return connection_no_transaction_cursor
    return connection_transaction_cursor
