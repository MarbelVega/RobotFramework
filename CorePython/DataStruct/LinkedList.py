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
