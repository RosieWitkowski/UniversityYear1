# Pseucodoce task 2: age verification
'''
START
    FUNCTION verify_age(age):
        IF age >= 18:
            return True 
        ELSE:
            return False 
    END FUNCTION
END
'''

# Flowchart text layout
'''
[Start]
    |
    v
[Input age]
    |
    v
[Is age >= 18?] -- Yes --> [Return True]
    |
    v
[Return False]
    |
    v
    [End]
'''

def verify_age(age):
    return True if age >= 18 else False 

print(verify_age(20))
print(verify_age(10))

