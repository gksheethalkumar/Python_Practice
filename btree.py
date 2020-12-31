class node():
    def __init__(self,data = None):
        self.data = data
        self.rightval= None
        self.leftval = None


    def insert(self,data = None):
        newval = node(data)

        if self.data:
            if data < self.data:
                if self.leftval is None:
                    self.leftval = newval
                else:
                    self.leftval.insert(data)

            if data > self.data:
                if self.rightval is None:
                    self.rightval = newval
                else:
                    self.rightval.insert(data)

        else:
            self.data = data

    def print_tree(self):
        if self.leftval:
            self.leftval.print_tree()
        print(self.data)

        if self.rightval:
            self.rightval.print_tree()

    def in_order(self,root):
        '''
        Left --> Root --> Right
        '''
        res = []
        if root:
            res = self.in_order(root.leftval)
            res.append(root.data)
            res = res + self.in_order(root.rightval)

        return res


    def pre_order(self,root):
        ''' Root --> left --> right '''
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order(root.leftval)
            res = res + self.pre_order(root.rightval)

        return res

    def post_order(self,root):
        ''' left --> right --> root'''
        res = []
        if root:
            res = self.post_order(root.leftval)
            res = res + self.post_order(root.rightval)
            res.append(root.data)
        return res

root = node()
root.insert(4)
root.insert(1)
root.insert(2)
root.insert(6)

root.print_tree()

print(root.in_order(root))
print(root.pre_order(root))
print(root.post_order(root))
