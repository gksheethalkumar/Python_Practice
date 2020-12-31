class node():
    def __init__(self,value=None):
        self.value = value
        self.nextval = None
        self.prevval = None


class DoubleLinkedList():
    def __init__(self):
        self.headval = None


    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.value)
            printval = printval.nextval


    def push(self,value=None):
        newval = node(value)
        newval.nextval = self.headval
        if self.headval is not None:
            self.headval.prevval = newval
        self.headval =  newval
        
    def append(self,value=None):
        newval = node(value)
        printval = self.headval
        while printval is not None:
            lastval = printval
            printval = printval.nextval
        lastval.nextval = newval
        newval.prevval = lastval

e1 = node("mon")
e2 = node("wed")
e3 = node("tue")


llist = DoubleLinkedList()
llist.headval = e1

e1.nextval = e3
e3.nextval = e2
e3.prevval = e1
e2.prevval = e3

#llist.print_list()

llist.push("sun")
#llist.print_list()

llist.append("thur")
llist.print_list()
