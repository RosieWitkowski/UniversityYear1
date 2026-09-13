def insertion_sort(list_example):
    copy_list = list_example[::]
    length = len(copy_list)
    for i in range(1, length):
        insert_index = i 
        current_val = copy_list.pop(i)
        for j in range(i-1, -1, -1):
            if copy_list[j] > current_val:
                insert_index = j 
        copy_list.insert(insert_index, current_val)
    return copy_list
