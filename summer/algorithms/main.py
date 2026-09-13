from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

default = [0, 5, 8, 2, 3, 7]
list_example = default

print("~ Bubble Sort ~")
print(f"Unsorted: {list_example}")
print(f"Sorted: {bubble_sort(list_example)}")

print ("~ Insertion Sort")
print(f"Unsorted: {list_example}")
print(f"Sorted: {insertion_sort(list_example)}")
