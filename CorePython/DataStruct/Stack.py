from collections import  deque
from array import array

#Implement Stack in Python
# Stack    ()       LIFO. Push to add, pop to remove (example undo or pile of books)
# Complexity O(1)

# ----------------------------------------------ARRAY-----------------------------------------------------#
num = array('d')
num.append(98)
print(num)  # num.append('AMIT') not allowed

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = Stack()
do = input('What would you like to do?').split()
operation = do[0].strip().lower()
if operation == 'push':
    s.push(int(do[1]))
elif operation == 'pop':
    if s.is_empty():
        print('Stack is empty')
    else:
        print('Popped value:', s.pop())

# Other option is using deque which use doubly linked lists
q = deque()
q.append('eat')
print(q)
q.pop()
