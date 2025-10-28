def celc_to_faren(celc):
    return (celc * 9/5) + 32

def valInt(msg):
    num = 'A'
    while not num.isnumeric():
        try:
            num = input(msg)
        except ValueError:
            print("Please enter an integar.")
    return int(num)

celc = valInt("Temperature in celcius: ")

faren = celc_to_faren(celc)
print(f"Temp: {faren}")

print(celc_to_faren(28))
print(celc_to_faren(100))

