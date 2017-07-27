# use a BST to store numbers from a text file
class Node(object):
   
    def __init__(self,data): # node constructor
        self.right_child = None
        self.left_child = None
        self.data = data
        self.count = 0

    def get_node_data(self):
        return self.data


class BST(object):
    def __init__(self):
         self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, current_node):
        if data < current_node.data:
            if current_node.left_child is None:
                current_node.left_child = Node(data)
            else:
                self.insert_node(data, current_node.left_child)

        elif data > current_node.data:
            if current_node.right_child is None:
                current_node.right_child = Node(data)
            else:
                self.insert_node(data, current_node.right_child)

        elif data == current_node.data:
            current_node.count += 1

        else:
            print("Error something is wrong!")

    def inOrder(self, current_node):
        if current_node is not None:
            self.inOrder(current_node.left_child)
            print(current_node.get_node_data())
            self.inOrder(current_node.right_child)

    def preOrder(self, current_node):
        if current_node is not None:
            print(current_node.get_node_data())
            self.preOrder(current_node.left_child)
            self.preOrder(current_node.right_child)

    def postOrder(self, current_node):
        if current_node is not None:
            self.postOrder(current_node.left_child)
            self.postOrder(current_node.right_child)
            print(current_node.get_node_data())




   
