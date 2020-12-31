class node():
    def __init__(self,value=None):
        self.value = value
        self.nextvalue = None


e1 = node("wed")
e2 = node("fri")
e3 = node("mon")
e4 = node("thu")
e5 = node("tue")

headvalue = e3
e3.nextvalue = e5
e5.nextvalue = e1
e1.nextvalue = e4
e4.nextvalue = e2


while headvalue is not None:
    print(headvalue.value)
    headvalue = headvalue.nextvalue

