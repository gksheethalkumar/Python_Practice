class node():
    def __init__(self,value=None):
        self.value = value 
        self.nextval = None




e1 = node("mon")
e2 = node("wed")
e3 = node("tue")



class SinLinkList():
    def __init__(self):
        self.headval = None
    
    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.value)
            printval = printval.nextval

    def addvalue_begin(self,value=None):
        newnode = node(value)
        newnode.nextval = self.headval
        self.headval = newnode

    def addvalue_end(self,value= None):
        newnode = node(value)
        printval = self.headval
        while printval is not None:
            lastval = printval
            printval = printval.nextval
        lastval.nextval = newnode

    def addvalue_mid(self,mid,value=None):
        newnode = node(value)
        newnode.nextval = mid.nextval
        mid.nextval = newnode

    def remove_value(self,value=None):
        printval = self.headval
        self.value = value
        while printval is not None:
            prev = printval
            printval = printval.nextval
            if printval.value is self.value:
                prev.nextval = printval.nextval
                break

llist = SinLinkList()
llist.headval = e1
llist.headval.nextval = e3
e3.nextval = e2
#llist.print_list()

llist.addvalue_begin("sun")

#llist.print_list()

llist.addvalue_end("thur")
llist.addvalue_end("fri")
#llist.print_list()

llist.addvalue_mid(e3,"middle")
#llist.print_list()
llist.remove_value("wed")
llist.print_list()
