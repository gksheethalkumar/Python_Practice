def log(func):
    print("#################")
    func()
    print('#################')

@log
def sayhi():
    print("Printing output")

@log
def sayno():
    print("Print Inout")



