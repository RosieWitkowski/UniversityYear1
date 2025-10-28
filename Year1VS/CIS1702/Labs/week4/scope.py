global_var = "Global variable"

def scope_test():
    global_var = "Local variable"
    print(global_var)

scope_test()
print(global_var)

