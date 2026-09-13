list_example = [0, 5, 8, 2, 3, 7]
counter, swaps, length = 0, 1 , len(list_example)

print(f"Unsorted: {list_example}")

while swaps > 0:
    counter, swaps = 0, 0 
    for i in range(0, length-1):
        if list_example[i] > list_example[i+1]:
            temp = list_example[i]
            list_example[i] = list_example[i+1]
            list_example[i+1] = temp 
            swaps += 1

print(f"Sorted: {list_example}")


    
