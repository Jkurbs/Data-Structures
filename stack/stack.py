"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

array = ["Computer science", "Physics", "Bioengineer", "Alternative Energy Engineer"]


class Stack:
    def __init__(self, storage):
        self.size = 0
        self.storage = storage

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        if value not in self.storage: 
            self.storage.append(value)
        pass

    def pop(self):
        self.storage.pop()
        pass


stack = Stack(array) 

stack.push("Physics")
print("Stack", stack.storage)