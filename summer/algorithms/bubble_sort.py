def bubble_sort(list_example):
    copy_list = list_example[::]
    swaps, length = 1, len(copy_list)
    while swaps > 0:
        swaps = 0
        for i in range(0, length-1):
            if copy_list[i] > copy_list[i+1]:
                temp = copy_list[i]
                copy_list[i] = copy_list[i+1]
                copy_list[i+1] = temp 
                swaps += 1
    return copy_list

def descending_bubble_sort(list_example):
    copy_list = list_example[::]
    swaps, length = 1, len(copy_list)
    while swaps > 0:
        swaps = 0
        for i in range(0, length-1):
            if copy_list[i] < copy_list[i+1]:
                temp = copy_list[i]
                copy_list[i] = copy_list[i+1]
                copy_list[i+1] = temp 
                swaps += 1
    return copy_list
    


    
