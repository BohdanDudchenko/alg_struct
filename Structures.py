from AbstractModule import AbstractStructure
from main import Generator, Person


class List(AbstractStructure):
    __list = []
    size = 0

    def add(self, value: Person, index: int = None) -> bool:
        if value is not None and index is None:
            self.__list.append(value)
            self.size = len(self.__list)
            return True
        elif value is not None and index in range(len(self.__list)):
            self.__list.insert(index, value)
            self.size = len(self.__list)
            return True
        else:
            return False

    def insert(self, value: Person, index: int) -> bool:
        if index not in range(len(self.__list)):
            return False
        else:
            self.__list[index] = value
            return True

    def remove(self, value: Person) -> bool:
        if value in self.__list:
            self.__list.remove(value)
            self.size = len(self.__list)
            return True
        else:
            return False

    def sort(self) -> bool:
        self.__list.sort()
        return True

    def get_all(self) -> list:
        return self.__list

    def get(self, index: int) -> object:
        if index in range(len(self.__list)):
            return self.__list[index]
        else:
            return None

    def find(self, value: Person) -> [int, None]:
        if value in self.__list:
            return self.__list.index(value)
        else:
            return None

    def __repr__(self):
        return f"{self.__list}"


class DynamiqueArray(AbstractStructure):
    __array: list = [None]
    __size: int = 1
    length: int = 0

    def __memory_check(self) -> bool:
        if self.length == self.__size:
            self.__size *= 2
            new_array = [None] * self.__size
            for key, el in enumerate(self.__array):
                new_array[key] = el
            self.__array = new_array
            return True
        else:
            return False

    def add(self, value: Person, index: int = None) -> bool:
        self.__memory_check()
        if index is None:
            self.__array[self.length] = value
            self.length += 1
            return True
        elif index in range(self.length):
            pos = self.length - 1
            while pos >= index:
                self.__array[pos + 1] = self.__array[pos]
                pos -= 1
            self.__array[index] = value
            self.length += 1
            return True
        else:
            return False

    def insert(self, value: Person, index: int) -> bool:
        if index in range(self.length):
            self.__array[index] = value
            return True
        else:
            return False

    def remove(self, value: Person) -> bool:
        self.__memory_check()
        if value in self.__array:
            pos = 0
            deletion = False
            while pos < self.length:
                if value == self.__array[pos]:
                    deletion = True
                if deletion is True:
                    self.__array[pos] = self.__array[pos + 1]
                pos += 1
            self.length -= 1
            return True
        else:
            return False

    def get(self, index: int) -> object:
        if index in range(self.length):
            return self.__array[index]
        else:
            return None

    def get_all(self) -> list:
        list = []
        for num in range(self.length):
            list.append(self.__array[num])
        return list

    def find(self, value) -> [int, None]:
        if value in self.__array:
            for pos in range(self.length):
                if value == self.__array[pos]:
                    return pos
        else:
            return None

    @property
    def array(self):
        return self.__array

    def __repr__(self):
        list = []
        for num in range(self.length):
            list.append(self.__array[num])
        return f"{list}"
