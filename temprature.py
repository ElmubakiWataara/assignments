"""Write and run a Python program that asks the user for a temperature in Celsius and converts
and outputs the temperature in Fahrenheit. Ask the user to input the temperature"""


#temperature = input("What's your temperature'\n'")
def convert(degree):
    fah = (degree * 9/5)+32
    return fah

degree = int(input("whats your temperature'\n'"))
fah = convert(degree)
print(fah)

