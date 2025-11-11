def add(a, b):
    return a + b 

'''
# -- Unit Test -- 
print("Running tests... ")
assert add(2, 4) == 6
assert add(1, 7) == 8
print("Successfull!")

print("Testing error messages... ")
assert add(5, 8) == 50, 'Expected output was 13'
assert add(9, 100) == False, 'Expected output was an int, not bool' # Note won't reach because it returns on line 11
print("Unexpected")

'''

# -- Unit Test 2-- 
try:
    assert add(5, 2) == 100
except AssertionError:
    print("5+2 != 100")


# -- Unit Test 3 -- 
assert add(5, 2) == 100, '5+2 != 100' # Note, WILL reach because the earlier test catches the example rather than returning