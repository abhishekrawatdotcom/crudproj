class Node:



    def __init__(self, data):

        self.left = None
        self.right = None
        self.node = data


    def insert(self, data):

        if self.node:
            if data < self.node:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.node:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.node = data


    def Print_Tree(self):
        if self.left:
            self.left.Print_Tree()
        print(self.node , end=' ')
        if self.right:
            self.right.Print_Tree()


root = Node(18)
root.insert(5)
root.insert(6)
root.insert(2)
root.insert(24)
root.insert(28)
root.insert(2)
root.Print_Tree()
