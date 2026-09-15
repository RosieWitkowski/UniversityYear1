# Handles the use of various sorting algorithm files, to test/demonstrate they work correctly
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

default = [0, 5, 8, 2]
list_example = default

print("~ Bubble Sort ~")
print(f"Unsorted: {list_example}")
print(f"Sorted: {bubble_sort(list_example)}")

print ("~ Insertion Sort")
print(f"Unsorted: {list_example}")
print(f"Sorted: {insertion_sort(list_example)}")

print ("~ Merge Sort")
print(f"Unsorted: {list_example}")
print(f"Sorted: {merge_sort(list_example)}")
