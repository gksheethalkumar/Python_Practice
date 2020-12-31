class node():
    def __init__(self,data = None):
        self.data = data
        self.rightval = None
        self.leftval = None


    def insert_tree(self,data = None):
        newval = node(data)

        if self.data:
            if data < self.data:
                if self.leftval is None:
                    self.leftval = newval
                else:
                    self.leftval.insert_tree(data)

            elif data > self.data:
                if self.rightval is None:
                    self.rightval = newval
                else:
                    self.rightval.insert_tree(data)

        else:
            self.data = data


    def print_tree(self):
        if self.leftval:
            self.leftval.print_tree()

        print(self.data)

        if self.rightval:
            self.rightval.print_tree()


root = node()
root.insert_tree(6)
root.insert_tree(2)
root.insert_tree(4)
root.insert_tree(7)
root.insert_tree(1)

root.print_tree()

