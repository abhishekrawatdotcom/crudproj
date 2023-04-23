class node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insertdata(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)

                else:
                    self.left.insertdata(data)

            if data > self.data:
                if self.right is None:
                    self.right = node(data)

                else:
                    self.right.insertdata(data)
        else:
            self.data = data


    def printdata(self):
        if self.left:
            self.left.printdata()
        print(self.data)

        if self.right:
            self.right.printdata()


root = node(30)
root.insertdata(1000)
root.insertdata(11)
root.insertdata(19)
root.insertdata(40)
root.insertdata(90)
root.printdata()




            



