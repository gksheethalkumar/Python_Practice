class node():
    def __init__(self,value=None):
        self.value = value
        self.nextval = None

class LinkedList():
    def __init__(self):
        self.headval = None
    def insert_beg(self,value=None):
        newval = node(value)
        newval.nextval = self.headval
        self.headval = newval

    def insert_end(self,value=None):
        newval = node(value)
        print_val = self.headval
        while print_val is not None:
            nxtval = print_val
            print_val = print_val.nextval
            if print_val is None:
                nxtval.nextval = newval

    def remove(self,value=None):
        print_val = self.headval

        while print_val  is not None:
            curr = print_val
            print_val = print_val.nextval
            val = print_val.value
            if val is value:
                curr.nextval = print_val.nextval
                break

    def print_val(self):
        print_val = self.headval
        while print_val is not None:
            print(print_val.value)
            print_val = print_val.nextval

e1 = node("mon")
e2 = node("wed")
e3 = node("tue")

llist = LinkedList()
llist.headval = e1

llist.headval.nextval = e3
e3.nextval = e2

llist.print_val()

llist.insert_beg("sun")
llist.print_val()
llist.insert_end("thur")
llist.print_val()
llist.remove("wed")
llist.print_val()
