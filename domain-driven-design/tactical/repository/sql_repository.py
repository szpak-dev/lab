from base_repository import BaseRepository


class SqlClient:
    def run(self, parameter):
        pass


class SqlRepository(BaseRepository):
    """Base class for all Sql-related Repositories with mandatory methods implemented"""
    query_runner = SqlClient()

    def get_by_id(self, id):
        return self.query_runner.run(id)

    def save(self, aggregate):
        return self.query_runner.run(aggregate)

    def remove(self, id):
        return self.query_runner.run(id)
