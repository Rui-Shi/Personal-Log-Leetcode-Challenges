# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

import random

class RandomizedSet:

    def __init__(self):
        self.val_map = {}  # Dictionary to store value: index pairs for O(1) lookup
        self.val_list = []  # List to store the values for getRandom()

    def insert(self, val: int) -> bool:
        if val in self.val_map:  # Check if the value already exists
            return False  # Return False if the value is already present

        self.val_map[val] = len(self.val_list)  # Store the index of the new value
        self.val_list.append(val)  # Add the value to the list
        return True  # Return True if the value was inserted

    def remove(self, val: int) -> bool:
        if val not in self.val_map:  # Check if the value exists
            return False  # Return False if the value is not present

        index_to_remove = self.val_map[val]  # Get the index of the value to remove
        last_element = self.val_list[-1]  # Get the last element in the list

        # Swap the element to be removed with the last element for O(1) removal
        self.val_list[index_to_remove] = last_element
        if index_to_remove != len(self.val_list) -1: # Avoid self swap in case of last element.
            self.val_map[last_element] = index_to_remove  # Update the index of the swapped element

        self.val_list.pop()  # Remove the last element (which was originally at index_to_remove)
        del self.val_map[val]  # Remove the value from the dictionary
        return True  # Return True if the value was removed

    def getRandom(self) -> int:
        return random.choice(self.val_list)  # Return a random element from the list