def bubble_sort(list):

    for idx in range(len(list) - 1, 0 , -1):
        for ele in range(idx):
            if list[ele] > list[ele+1]:
                temp = list[ele]
                list[ele] = list[ele+1]
                list[ele+1] = temp

    return list
print(bubble_sort([4,2,34,56,2,4,6,23,4,65]))

