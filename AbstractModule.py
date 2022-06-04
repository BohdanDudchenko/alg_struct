from abc import ABC, abstractmethod


class AbstractStructure(ABC):

    @abstractmethod
    def add(self, value, index) -> bool:
        ...

    @abstractmethod
    def insert(self, value, index) -> bool:
        ...

    @abstractmethod
    def find(self, value) -> [int, None]:
        ...

    @abstractmethod
    def get(self, index) -> object:
        ...

    @abstractmethod
    def remove(self, value) -> bool:
        ...

    @abstractmethod
    def get_all(self) -> list:
        ...

