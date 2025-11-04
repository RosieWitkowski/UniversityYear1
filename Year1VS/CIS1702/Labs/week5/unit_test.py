# Implementing a basic test plan on a code from last week, using assert
def celc_to_faren(celc):
    return (celc * 9/5) + 32

"""
Test Plan for celsius_to_fahrenheit:
1. Test freezing point: 0C should be 32F.
2. Test boiling point: 100C should be 212F.
3. Test room temperature: 25C should be 77F.
"""

# --- Unit Tests --- 
print("Running tests...")

assert celc_to_faren(0) == 32 
assert celc_to_faren(100) == 212
assert celc_to_faren(25) == 77

# Intentional bug for testing:
# assert celc_to_faren(25) == 10000

print("All tests successfully passed.")
