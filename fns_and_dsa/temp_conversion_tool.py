FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{fahrenheit}°F is {celsius}°C"
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return f"{celsius}°C is {fahrenheit}°F"

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if unit == "C":
    print(convert_to_celsius(temperature))
elif unit == "F":
    print(convert_to_fahrenheit(temperature))
else:
    print("Invalid temperature. Please enter a numeric value.")