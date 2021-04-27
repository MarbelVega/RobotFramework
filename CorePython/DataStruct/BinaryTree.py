# Non-linear data structure with root and child nodes to left and right




class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:

    def createNode(self, data):
        return Node(data)

    def insert(self, node , data):
        # Insert function will insert a node into tree.Duplicate keys are not allowed.

        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node

    def traverseInorder(self, root):                  # left-root-right
        if root is not None:
            self.traversePostorder(root.left)
            print(root.data)
            self.traversePostorder(root.right)


    def getSize(self, root):
        if root == None:
            return 0
        else:
            return self.getSize(root.left) + 1 + self.getSize(root.right)


tree = BinaryTree()
root = Node(12)
print(root)
tree.insert(root, 20)
tree.insert(root, 30)
tree.insert(root, 4)
tree.insert(root, 70)
tree.insert(root, 6)
tree.insert(root, 80)

print("TRAVERSAL")
tree.traverseInorder(root)

print("SIZE - ", tree.getSize(root))