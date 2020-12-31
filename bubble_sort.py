class sort():
    def __init__(self,list= None):
        self.list = list

    def bsort(self,list):
        '''
        sort
        for i in range(first,last, step ) 
        for i in range( last element,first element, step ( reverse -1 ) )
        '''
        for i in range(len(list) - 1, 0 , -1):
            for idx in range(i):
                if list[idx] > list[idx+1]:
                    temp = list[idx]
                    list[idx] = list[idx+1]
                    list[idx+1] = temp

        return(list)

list = [3,1,3,5,8,2,4.5,83]

test = sort()
print(test.bsort(list))
