from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        """raise NotImplementedError("__init__ method not implemented")"""
        self.__bag: dict[T, int] = {}
        """int tells us the count, T are representing all the items as called type"""

        """if items is not None:
            for item in items:
                if item in self.__bag:
                    self.__bag(item) +=1
                else:
                    self.__bag(item) = 1 
        want to see if key does exist in dictionary, then I'll set counter at one, if item 
        DNE yet, then just want to count by 1 every time new item is added"""
        """expect that all methods mentioned in ibag are explained/written here"""

    def add(self, item: T) -> None:
        raise NotImplementedError("add method not implemented")
        """if item in self.__bag:
                self.__bag(item) +=1
            else:
                self.__bag(item) = 1 """ 
    def remove(self, item: T) -> None: 
        raise NotImplementedError("remove method not implemented")

    def count(self, item: T) -> int:
        raise NotImplementedError("count method not implemented")

    def __len__(self) -> int:
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> int:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")