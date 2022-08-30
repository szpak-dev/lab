from abc import ABC, abstractmethod


class BaseRepository(ABC):
    """Interface with minimum set of methods for all Repositories"""
    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def save(self, aggregate):
        pass

    @abstractmethod
    def remove(self, id):
        pass
