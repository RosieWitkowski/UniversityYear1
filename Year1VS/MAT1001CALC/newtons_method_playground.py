"""
Personal version of n-r method code, with a generic fn for ordered equations and a specific for sine,cos
Purely for experimentation, see newtons_method_cw for the one required for MAT1001 CW1 question 3c
"""
import math 


def main():
    # USING EQUATION FROM SHEET, CHANGE FOR CW
    # Fn and d/dx are formatted as (coefficient, exponent) e.g. [(4, 3), (-2, 1)] == 4x**3 -2x**1 = 4x^3 - 2x 
    print("Solution for x^5 + 7x^3 - 2 = 0")
    xn, max = .6, .7 
    function, derivative = [(1, 5), (7, 3), (-2, 0)], [(5, 4), (21, 2)]

    print(f"Answer = {newton_method(xn, max, function, derivative):.5f}") # Displayed to 5 decimal places

def newton_method(xn, max, function, derivative):
    """Iteratively applies Newton Raphson formula until the root is found."""
    while xn < max:
        # Use formula to find xn+1
        xn = nr_formula(xn, function, derivative)
        xn_next = nr_formula(xn, function, derivative)

        # Solution is found 
        if xn_next - xn == 0:
            return xn
        

def nr_formula(xn, function, derivative):
    """Applies the formula xn+1 = xn - (f(xn) / f'x(n)), returning the answer"""
    f_x, f_prime_xn = 0, 0

    # Calculates f(x) and f'(x) for xn
    for operation in function:
        # e.g. 4x^3 for x = 2, == (2 ** 3) * 4
        f_x +=  ( (xn ** operation[1])  * operation[0])

    for operation in derivative:
        f_prime_xn += ( (xn ** operation[1])  * operation[0])


    # Exits early if the derivative approaches zero for xn
    if f_prime_xn == 0:
        print("Will not converge to root as f'(xn) -> 0 and 1/0 is undefined.")
        exit()

    # Uses the calculated f(x) and f'(x) in the formula, for an answer
    return xn - ( (f_x) / (f_prime_xn) )

if __name__ == "__main__":
    main()


def nr_method_sin(xn):
    # Applies the formula xn+1 = xn - (f(xn) / f'x(n)), returning the answer

    # Calculates f(x) and f'(x) for xn
    f_x = (3* xn) - (4 * (math.cos(xn)) ) # Consider whether to use math.radians(xn)

    f_prime_xn = 3 + (4 * (math.sin(xn)))

    # Exits early if the derivative approaches zero for xn
    if f_prime_xn == 0:
        print("Will not converge to root as f'(xn) -> 0 and 1/0 is undefined.")
        exit()

    # Uses the calculated f(x) and f'(x) in the formula, for an answer
    return xn - ( (f_x) / (f_prime_xn) )

print("3x - 4cosx = 0")
xn, max = .8, .9
while xn < max:
    xn = nr_method_sin(xn)
    xn_next = nr_method_sin(xn)
    print(xn, xn_next)

    # Solution is found 
    if xn_next - xn == 0:
        print(f"Answer: {xn}")
        exit()