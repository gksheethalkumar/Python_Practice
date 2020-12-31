class node():
    def __init__(self,value = None):
        self.value = value


    def search(self,list,value=None):
        idx0 = 0 
        idxn = len(list) - 1

        while idx0 <= idxn:
            midval = (idx0 + idxn) //2

            if list[midval] == value:
                return midval

            if value > list[midval]:
                idx0 = midval + 1
            else:
                idxn = midval - 1

        if idx0 > idxn:
            return None

    def bsort(self,list):
        for i in range(len(list) - 1, 0 , -1):
            for idx in range(i):
                if list[idx] > list[idx+1]:
                    temp = list[idx]
                    list[idx] = list[idx+1]
                    list[idx+1] = temp

        return list

list = [13,1,5,7,2,3,4,5,7,8,3,0,7,8,9]
root = node(5)
print(root.bsort(list))
print(root.search(list,4))
print(root.search(list,12))


