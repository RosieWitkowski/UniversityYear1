"""Applies Newton's Raphson Method to solve the equations e^-x - x = 0, and xe^-x + 1 = 0"""
import math 

def main():
    print('+-- Equation 1--+')
    # Equation 1
    print("e^-x - x = 0")
    xn, max = .5, 1 # Max of 1 based on how the graph diverges, increasingly negative away from 0
    print(f"Solution = {newton_method(xn, max, 'eq1'):.5f}") # Displayed to 5 decimal places

    print('\n+-- Equation 2--+')
    # Equation 2
    print("xe^-x + 1 = 0")
    xn, max = -.6, 1 # Max of 1 based on graph, moves away from 0 and remains positive
    print(f"Solution = {newton_method(xn, max, 'eq2'):.5f}") 

def eq1(xn):
    """Returns e^-x - x and its derivative, at the point xn"""
    equation = math.exp(-xn) - xn 
    derivative = (-1 * (math.exp(-xn)) ) - 1
    return equation, derivative

def eq2(xn):
    """Returns  xe^-x + 1 and its derivative, at the point xn"""
    equation = (xn * (math.exp(-xn)) ) + 1 
    derivative = math.exp(-xn) - (xn * (math.exp(-xn)))
    return equation, derivative

def newton_method(xn, max, equation):
    """Iteratively applies Newton Raphson formula until the root is found."""
    while xn < max:
        if equation == 'eq1':
            fn, derivative = eq1(xn)
        else:
            fn, derivative = eq2(xn)

        # Use the formula to find xn+1
        xn = nr_formula(xn, fn, derivative)
        xn_next = nr_formula(xn, fn, derivative)

        # Solution is found 
        if xn_next - xn == 0:
            return xn

def nr_formula(xn, fn, derivative):
    """Applies the formula xn+1 = xn - (f(xn) / f'x(n)), returning the answer"""
    # Exits early if the derivative approaches zero for xn
    if derivative == 0:
        print("Will not converge to root as f'(xn) -> 0 and 1/0 is undefined.")
        exit()

    # Uses the calculated f(x) and f'(x) in the formula, for an answer
    return xn - ( (fn) / (derivative) )

if __name__ == "__main__":
    main()