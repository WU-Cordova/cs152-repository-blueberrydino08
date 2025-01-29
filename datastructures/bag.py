from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    #for a specific bag, everything needs to have the same type, using T will only work if same type
    #star unpacks items
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        #              key, value
        #self is the bag
        self._bag: dict[T, int] = {}
        if items is not None: 
            for item in items: 
                self.add[item]
       
    #                         returns nothing because we don't need a "false" or "true" answer
    def add(self, item: T) -> None:
        if item is None:
            raise TypeError("Item is not valid and cannot be added to bag.")
            #if error is raised, doesn't continue the code
        if item in self._bag:
            self._bag[item] += 1 
            "if the same item name is already there, just the count will increase-> I don"
        else:
            self._bag[item] = 1

    def remove(self, item: T) -> None:
        if item not in self._bag:
            raise ValueError("Item is not in the bag.")
        if item in self._bag:
            #              if it is =- 1 it will set self._bag[self] to the value of -1
            # decreasing the count of that specific item
            self._bag[item] -= 1
            """if self is the key, we can specify what we want to take out of the bag and then
            decrese the count? I am not removing entirely, right? Just decreasing..."""


    def count(self, item: T) -> int:
        if item not in self._bag:
            return 0 
        #if it hits the first statement then it won't run the next one
        else:
            return self._bag[item] 
        
        """._bag is the dictionary with the [item] as the value part of the key-value pair"""

    def __len__(self) -> int:
        #don't need to do the total variable 
        total = sum(self._bag.values())
        return total 

    def distinct_items(self) -> set[int]:
        #set can return unique values but is not affecting original dictionary 
        return set(self._bag.keys())

    def __contains__(self, item) -> bool:
        #"in" will already evaluate if this is true or false 
        return item in self._bag
    
        """if item in self._bag: 
                return True
            else: 
                return False"""
      
    def clear(self) -> None:
        self._bag.clear()
        
        """empty_dictionary = {}
           self._bag = empty_dictionary
        """