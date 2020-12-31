class node():
    def __init__(self, value = None):
        self.value = value
        self.rightval = None
        self.leftval = None

    def bstree(self, root):
        
        def dfs(root,path):

            if not root.leftval and not root.rightval:
                paths.append(path)

            if root.leftval:
                dfs(root.leftval, path + "->" + str(root.leftval.value))
            if root.rightval:
                dfs(root.rightval, path + "->" + str(root.rightval.value))


        paths = []
        if not root:
            return paths

        dfs(root, str(root.value))

        return paths

    def btree(self,value= None):
        newval = node(value)
        if self.value:
            if value < self.value:
                if self.leftval is None:
                    self.leftval = newval
                else:
                    self.leftval.btree(value)

            elif value > self.value:
                if self.rightval is None:
                    self.rightval = newval
                else:
                    self.rightval.btree(value)
        else:
            self.value = value

    def print_tree(self):
        if self.leftval:
            self.leftval.print_tree()
        print(self.value)
        if self.rightval:
            self.rightval.print_tree()
root = node(1)
root.btree(2)
root.btree(5)
root.btree(3)

print(root.bstree(root))
