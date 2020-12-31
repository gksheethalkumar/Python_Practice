class solution():
    def __init__(self,list=[]):
        self.list = list

    def bstree(self,value = None):

        idx0 = 0
        idxn = len(self.list) - 1
        while idx0 <= idxn:

            midval = ( idx0 + idxn ) //2

            if self.list[midval] == value:
                return midval

            if value < self.list[midval]:
                idxn = midval -1
            else:
                idx0 = midval + 1

        if idx0 > idxn:
            return None

list = [0,1,2,3,4,5,6,7,8]
l = solution(list)
print(l.bstree(5))
