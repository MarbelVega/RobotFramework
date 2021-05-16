# LinkedList      [] Linear, each element stores data and next. Last node points to null.
# Complexity - O(1) for insert, can be 1 or n for search depending on location of element.

class Node(object):
    # Constructor to initialize class variables
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


# Initialize the list with head
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # create new node and make it head
    def insert(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    # traverse to search by data or index
    def search(self, nodeData, index):
        prv = None
        temp = self.head
        while (temp and temp.data != nodeData):
            prv = temp
            temp = temp.next_node

        if temp is None:
            raise ValueError("Not present")
        return temp

        # search by index
        for i in range(0, index, 1):
            temp = temp.next_node
        return temp

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next_node

    def delete(self, nodeData, node):
        prv = None
        temp = self.head
        while temp and temp.data != nodeData:
            prv = temp
            temp = temp.next_node

        # Simply unlink
        prv.next_node = temp.next_node

        # When node to be deleted is passed, we copy next node data and leapfrog that.

        temp = node.next_node
        node.data = temp.data
        node.next_node = temp.next_node
        temp = None

    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        # While both list exists
        while(first is not None or second is not None):
            fdata = sdata = 0

            # Move first and second pointers to next nodes
            if first is not None:
                fdata = first.data
                first = first.next_node
            if second is not None:
                sdata = second.data
                second = second.next_node

            Sum = carry + fdata + sdata

            # update carry for next calculation
            carry = 1 if Sum >= 10 else 0

            # update sum if it is greater than 10
            Sum = Sum if Sum < 10 else Sum % 10

            # Create a new node with sum as data
            temp = Node(Sum)

            # if this is the first node then set it as head of resultant list

            if self.head is None:
                self.head = temp
            else:
                prev.next_node = temp

            # Set prev for next insertion
            prev = temp

        if carry > 0:
            temp.next_node = Node(carry)


# Given two numbers represented by two lists, write a function that returns the sum list

first = LinkedList()
second = LinkedList()
first.insert(6)       # 9->4->6 = 649
first.insert(4)
first.insert(9)
print("First Node \n")
first.print()
second.insert(5)      # 7->5 = 57
second.insert(7)
print("Second Node \n")
second.print()
res = LinkedList()
res.addTwoLists(first.head, second.head)
print("Sum Node \n")
res.print()