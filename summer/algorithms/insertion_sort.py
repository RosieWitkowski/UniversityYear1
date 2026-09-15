# Moves elements to the correct position, by comparing to previous elements (building a 'sorted' left)
# O(n^2), Ω(n), Space O(1)
def insertion_sort(list_example):
    copy_list = list_example[::]
    length = len(copy_list)
    for i in range(1, length):
        insert_index = i 
        current_val = copy_list[i] 
        for j in range(i-1, -1, -1): # Backwards, splitting into sorted left 
            if copy_list[j] > current_val:
                copy_list[j+1] = copy_list[j] # Copies higher elements forward
                insert_index = j # Update j to one before the copy
            else:
                break
        copy_list[insert_index] = current_val 
    return copy_list

# O(n^2), Ω(n), Space O(1)
def descending_insertion_sort(list_example):
    copy_list = list_example[::]
    length = len(copy_list)
    for i in range(1, length):
        insert_index = i 
        current_val = copy_list[i] 
        for j in range(i-1, -1, -1):
            if copy_list[j] < current_val:
                copy_list[j+1] = copy_list[j]
                insert_index = j 
            else:
                break
        copy_list[insert_index] = current_val
    return copy_list
