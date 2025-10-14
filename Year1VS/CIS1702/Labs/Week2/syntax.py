""" 
This program converts a given temperature in celcius to fahrenheit. 
"""

def convert(temp):
    tempF = (temp * 9/5) + 32  # This is the formula for converting celcius to fahrenheit 
    print(f"{tempF} F")
    return tempF

convert(-5)
convert(20)
convert(32.4)
convert(40)  # Print displays the output in the terminal

"""
Changing the argument for the convert fn means that different value is now used to perform the calculation; a higher temperature in celcius will result in a higher temperature in fahrenheit.
"""