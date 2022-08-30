import connector
from psycopg2 import extensions as ext

connection = connector.connection(no_transaction=True)
cursor = connection.cursor()


def with_read_committed():
    connection.set_isolation_level(ext.ISOLATION_LEVEL_READ_COMMITTED)
    return connection


def with_repeatable_read():
    connection.set_isolation_level(ext.ISOLATION_REPEATABLE_READ)
    return connection


def with_serializable():
    connection.set_isolation_level(ext.ISOLATION_LEVEL_SERILIZABLE)
    return connection
