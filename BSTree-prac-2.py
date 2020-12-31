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


    def search(self,data = None):

        if data < self.data:
            if self.leftval is None:
                return ( str(data) + " Not found")
            return (self.leftval.search(data))

        elif data > self.data:
            if self.rightval is None:
                return ( str(data) + " Not Found")
            return (self.rightval.search(data))

        else:
            return ( str(data) + " is found")


root = node()
root.insert_tree(4)
root.insert_tree(1)
root.insert_tree(6)
root.insert_tree(2)
root.insert_tree(5)

print(root.search(4))
print(root.search(7))
