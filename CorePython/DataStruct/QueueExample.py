# Queue       {}   FIFO. Enqueue and dequeue elements, has max size (example call center, luggage belt)
# Complexity - O(n) for display else O(1)

class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    # returns bool value whether queue is full to check b4 enqueue
    def is_full(self):
        if self.__rear == self.__max_size - 1:
            return True
        return False

    # function to check if queue is empty b4 dequeue
    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!!!")
        else:
            self.__front += 1
            data = self.__elements[self.__front]
            return data

    # function to display elements from front to rear if queue is not empty
    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size
