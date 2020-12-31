class node():
    def __init__(self,value=None):
        self.value = value
        self.rightval = None
        self.leftval = None

    def insert(self,value=None):
        newval = node(value)

        if self.value:
            if value < self.value:
                if self.leftval is None:
                    self.leftval = newval
                else:
                    self.leftval.insert(value)

            elif value > self.value:
                if self.rightval is None:
                    self.rightval = newval
                else:
                    self.rightval.insert(value)

        else:
            self.value = value


    def print_tree(self):
        if self.leftval:
            self.leftval.print_tree()
        print(self.value)
        if self.rightval:
            self.rightval.print_tree()

root = node(4)
root.insert(6)
root.insert(12)
root.insert(3)

root.print_tree()

