from bubble_sort import bubble_sort, descending_bubble_sort
from insertion_sort import insertion_sort, descending_insertion_sort

default = [0, 5, 8, 2]
list_example = default

print("~ Bubble Sort ~")
print(f"Unsorted: {list_example}")
print(f"Sorted: {bubble_sort(list_example)}")

print("~ Descending Bubble Sort ~")
print(f"Unsorted: {list_example}")
print(f"Sorted: {descending_bubble_sort(list_example)}")

print ("~ Insertion Sort")
print(f"Unsorted: {list_example}")
print(f"Sorted: {insertion_sort(list_example)}")

print ("~ Descending Insertion Sort")
print(f"Unsorted: {list_example}")
print(f"Sorted: {descending_insertion_sort(list_example)}")
