import connector
from pathlib import Path

path = '/opt/data'
cursor = connector.cursor(no_transaction=True)


def run_script(filename):
    abs_path = '{path}/{filename}.sql'.format(path=path, filename=filename)
    query = Path(abs_path).read_text()

    cursor.execute(query)
