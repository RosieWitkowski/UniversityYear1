# Building on basic triangle printing, to produce a slightly more complex array print

height = 4

print("+ == RIGHT-ALIGNED == +")
gap = height
length = 0
while gap > 0:
    gap -= 1
    length += 1
    print(" "*gap, "#"*length)

print("+ == LEFT-ALIGNED == +")
length = 0
while length < height:
    length += 1
    print("#"*length)


print("+ == LEFT-ALIGNED NUMBER == +")
nums = [1, 2, 3, 4, 5, 6,7 ,8, 9, 10]
height = 4
length = 0
while length < height:
    length += 1
    for _ in range(length):
        print(nums[0], end=" ")
        nums.pop(0)
    print()

print("+ == MIDDLE-ALIGNED NUMBER == +")
nums = [1, 2, 3, 4, 5, 6,7 ,8, 9, 10]

gap = height
length = 0
while length < height:
    length += 1
    gap -= 1
    print(" " * gap, end="")
    for _ in range(length):
        print(nums[0], end=" ")
        nums.pop(0)
    print()

print("+ == RIGHT-ALIGNED NUMBER == +")
nums = [1, 2, 3, 4, 5, 6,7 ,8, 9, 10]

gap = height*2
length = 0
while length < height:
    length += 1
    gap -= 2
    print(" " * gap, end="")
    for _ in range(length):
        print(nums[0], end=" ")
        nums.pop(0)
    print()
    
    