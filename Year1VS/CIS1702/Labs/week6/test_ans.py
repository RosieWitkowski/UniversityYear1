# Looking at some of the answers from the test 2

# TASK: Predict output
counter = 5
while counter < 20:
    counter = counter + 3

print(counter) # Expected output: 20 | Explination: Last run is when counter is 17, so will add 3, at which point hits 20 limit

# TASK: Predict output
count = 0
for i in range(4):
    for j in range(2):
        count = count + 1
print(count) # Expected output: 8 | Explination: Runs 4 iterations of 2x(+1), 4*2 = 8


# TASK: Fill in the blank so prints even numbers 1 to 10 (inclusive)
for i in range(1, 11):
        if i % 2 == 0:
            print(i, end=" ")

# TASK: Predict output
x = 5
# assert x > 10, "Value must be greater than 10"
# AssertationError: Value must be greater than 10 

# Own experiments
assert x < 10
print("X less than 10")

try:
    assert x > 10
except AssertionError:
    print("X must be more than 10.")

assert x > 10, 'X is less than 10.'