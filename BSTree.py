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


    def search_val(self,value=None):

        if value < self.value:
            if self.leftval is None:
                return ( str(value) + " Not found")
            return(self.leftval.search_val(value))

        elif value > self.value:
            if self.rightval is None:
                return ( str(value) + " Not found")
            return(self.rightval.search_val(value))
        
        else:
            return(str(self.value) + " is found")


    def print_tree(self):
        if self.leftval:
            self.leftval.print_tree()

        print(self.value)

        if self.rightval:
            self.rightval.print_tree()


root = node()
root.insert(4)
root.insert(1)
root.insert(2)
root.insert(6)

root.print_tree()

print(root.search_val(7))
print(root.search_val(2))
