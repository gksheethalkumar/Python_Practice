def bsearch(list, idx0, idxn, val):

    if idx0 > idxn:
        return None
    else:
        midval = (idx0 + idxn)//2


        if list[midval] > val:
            return ( bsearch(list,idx0,midval-1,val))
        elif list[midval] < val:
            return ( bsearch(list, midval+1, idxn,val))
        else:
            return midval


print(bsearch([1,2,3,4,5],0,4,4))

