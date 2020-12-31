import heapq

l = [5,2,4,6,8,1,3,5,7,2,46,7,3]

lp = heapq.heapify(l)

smallest = heapq.nsmallest(3, l, key=None)
print(smallest)

print(heapq.nlargest(5,l,key=None))

heapq.heapreplace(l,8)

heapq.heappop(l)
print(l)
