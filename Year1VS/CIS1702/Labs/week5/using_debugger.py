def calculate_factorial(n):
    total = 1 # <-- Bug #1 Fix by changing total = 0 to total = 1 to prevent zero multiplication
    for i in range(1, n + 1):
        total = total * i # <-- Bug #2 (logic is flawed)
    return total

result = calculate_factorial(5)
print(f"5! is {result}") # Should be 120, but prints 0


