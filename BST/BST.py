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
        self.number_of_nodes = 0

    def insert(self, data):
        if self.root is None:
            self.number_of_nodes += 1
            self.root = Node(data)
        else:
            self.number_of_nodes += 1
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


    def print_inOrder(self, current_node):
        if current_node is not None:
            self.print_inOrder(current_node.left_child)
            print(current_node.get_node_data(), end = ", ")
            self.print_inOrder(current_node.right_child)

    def print_preOrder(self, current_node):
        if current_node is not None:
            print(current_node.get_node_data(), end = ", ")
            self.print_preOrder(current_node.left_child)
            self.print_preOrder(current_node.right_child)

    def print_postOrder(self, current_node):
        if current_node is not None:
            self.print_postOrder(current_node.left_child)
            self.print_postOrder(current_node.right_child)
            print(current_node.get_node_data())

    def number_of_nodes(self):
        return self.number_of_nodes

    def search_tree(self,current_node, item):
        if item == current_node.data:
            print("Found item")
            return item
        elif item < current_node.data:
            print("Too small")
            return self.search_tree(current_node.left_child, item)
        elif item > current_node.data:
            print("Too big")
            return self.search_tree(current_node.right_child,item)
        elif current_node.left_child is None and current_node.right_child is None and item != current_node.data :
            return "Not found in system!"
        else:
            return "Error"
def main():

    print("This is main.")
    f = open("numbers.txt", "r")
    tree = BST()
    random_number = f.readlines()
    for number in random_number:
        tree.insert(int(number))
    f.close()

    
main()

   
