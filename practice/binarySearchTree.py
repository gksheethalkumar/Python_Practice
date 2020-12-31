class node():
    def __init__(self,value=None):
        self.value = value
        self.rightval = None
        self.leftval = None

    def insert(self,value= None):

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

    def search(self,value = None):
        if value < self.value:
            if self.leftval is None:
                return(str(value) + " Not found")
            return ( self.leftval.search(value))

        elif value > self.value:
            if self.rightval is None:
                return ( str(value) + " Not found")
            return (self.rightval.search(value))

        return (str(value) + " found")

    def print_tree(self):
        if self.leftval:
            self.leftval.print_tree()
        print(self.value)
        if self.rightval:
            self.rightval.print_tree()


root = node(4)
root.insert(5)
root.insert(1)
root.insert(6)
print(root.search(1))
print(root.search(9))

root.print_tree()
