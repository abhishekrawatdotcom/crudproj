class treenode:
    def __init__(self ,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):

        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)

        for child in self.children:
            child.print_tree()



def build_prduct_tree(self):
    root = treenode('electrinic')
    laptop = treenode('laptops')
    laptop.add_child(treenode('mac'))
    laptop.add_child(treenode('surface'))
    laptop.add_child(treenode('thinkpad'))

    cellphone = treenode('cell phone')
    cellphone.add_child(treenode('iphone'))
    cellphone.add_child(treenode('oppo'))
    cellphone.add_child(treenode('vivo'))

    tv = treenode('tv')
    tv.add_child(treenode('samsung'))
    tv.add_child(treenode('song'))
    root.add_child(laptop)

    return print(tv)

if __name__ == '__main__':
    build_prduct_tree()

    


