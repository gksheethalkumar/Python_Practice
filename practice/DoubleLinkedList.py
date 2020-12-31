class node():
    def __init__(self,value=None):
        self.value = value
        self.nextval = None
        self.preval = None

class DoubleLList():
    def __init__(self):
        self.headval = None

    def push_first(self,value=None):
        newval = node(value)
        newval.nextval = self.headval
        if self.headval is not None:
            self.headval.preval = newval
        self.headval = newval


    def push_last(self,value=None):
        newval = node(value)

        printval = self.headval
        while printval is not None:
            curr = printval
            printval = printval.nextval
            if printval.nextval is None:
                printval.nextval = newval
                printval.preval = curr
                break

    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.value)
            printval = printval.nextval

dllist = DoubleLList()
dllist.push_first(12)
dllist.push_first(8)
dllist.push_last(62)
dllist.print_list()

