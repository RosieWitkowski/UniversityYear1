def insertion_sort(list_example):
    copy_list = list_example[::]
    length = len(copy_list)
    for i in range(1, length):
        insert_index = i 
        current_val = copy_list[i] 
        for j in range(i-1, -1, -1):
            if copy_list[j] > current_val:
                copy_list[j+1] = copy_list[j]
                insert_index = j 
            else:
                break
        copy_list[insert_index] = current_val
    return copy_list
