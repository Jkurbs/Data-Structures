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


# class Node: 

#     def __init__(self, value, next_node):
#         super().__init__()
#         self.value = value 
#         self.next_node = next_node
    
#     'Get the value of the given node'
#     def get_value(self, value): 
#         return self.value 
    
#     'Get the next node that the current node is pointing to'
#     def get_next(self): 
#         return self.next_node
    
#     'Set the next node'
#     def set_next(self, new_next):
#         self.next_node = new_next 



class Stack:

    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        count = len(self.storage)
        if count > 0:
            return count
        else: 
            return 0

    def push(self, value):
        if value not in self.storage: 
            self.storage.append(value)
        pass

    def pop(self):
        if len(self.storage) > 0: 
            return self.storage.pop()

    def remove_all(self): 
        self.storage.clear()



stack = Stack()

stack.push(100)
stack.push(101)
stack.push(105)

print("storage:", stack.storage)
print("length:", len(stack.storage))
