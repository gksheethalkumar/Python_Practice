class node():
    def __init__(self,value=None):
        self.value = value
        self.nextval = None




class LinkedList():
    def __init__(self):
        self.headvalue = None


    def printlist(self):
        printval = self.headvalue
        while printval is not None:
            print(printval.value)
            printval = printval.nextval


    def insert_beg(self,value=None):
        newval = node(value)
        newval.nextval = self.headvalue
        self.headvalue = newval


    def insert_end(self,value=None):
        newval = node(value)
        printval = self.headvalue
        while printval is not None:
            lastval = printval
            printval = printval.nextval
        lastval.nextval = newval 


    def insert_mid(self,mid,value=None):
        newval = node(value)
        printval = self.headvalue
        newval.nextval = mid.nextval
        mid.nextval = newval

    def remove_item(self,value=None):
        printval = self.headvalue
        while printval is not None:
            newval = printval
            ntval = newval.nextval
            printval = printval.nextval
            if ntval.value is value:
                newval.nextval = ntval.nextval
                break


e1 = node("mon")
e2 = node("wed")
e3 = node("tue")


llist = LinkedList()
llist.headvalue = e1
llist.headvalue.nextval = e3
e3.nextval = e2

#llist.printlist()


llist.insert_beg("sun")

#llist.printlist()

llist.insert_end("thur")

#llist.printlist()


llist.insert_mid(llist.headvalue.nextval,"middle")
llist.remove_item("wed")
llist.printlist()
