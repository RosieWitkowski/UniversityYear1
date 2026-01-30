# Some operations may change data in place, causing potential mutation leaks 

# Mutates original
scores = [78, 92, 45, 88]
print("Original: ", scores)
scores.sort()
print(scores)

# Creates new variable
scores = [54, 32, 90, 49]
print("Original: ", scores)
print(sorted(scores))
print(scores)
