# O(nlogn), Space O(n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr 

    mid = len(arr) // 2
    side_L, side_R = arr[:mid], arr[mid:]

    sorted_L, sorted_R = merge_sort(side_L), merge_sort(side_R)
    # print(sorted_L, sorted_R)
    return merge(sorted_L, sorted_R)

def merge(arr_L, arr_R):
    # print("MERGE", arr_L, arr_R)
    result = []
    pointer_L = pointer_R = 0

    while pointer_L < len(arr_L) and pointer_R < len(arr_R):
        if arr_L[pointer_L] < arr_R[pointer_R]:
            result.append(arr_L[pointer_L])
            pointer_L += 1 
        else:
            result.append(arr_R[pointer_R])
            pointer_R += 1

    result.extend(arr_L[pointer_L:])
    result.extend(arr_R[pointer_R:])
    # print("RESULT", result)
    return result 
