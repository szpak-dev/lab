from abc import ABC, abstractmethod
from typing import List


class MediatorEvent:
    pass


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str, data: List = []) -> None:
        pass


class MediatorComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator
