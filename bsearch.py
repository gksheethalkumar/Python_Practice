class solution():
    def __init__(self,listt = [], value = None):
        self.listt = listt
        self.value = value

    def search(self,value = None):
        self.value = value
        idx0 = 0
        idxn = len(self.listt) - 1

        while idx0 <= idxn:
            midval = (idx0 + idxn)//2

            if self.listt[midval] == self.value:
                return midval

            if self.value > self.listt[midval]:
                idx0 = midval + 1
            else:
                idx0 = midval - 1

        if idx0 > idxn:
            return None


llist = [1,2,3,4,5,6,7,8,9]
a = solution(llist)
print(a.search(5))
print(a.search(52423))
