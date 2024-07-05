FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    celcius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celcius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit= (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius)+32
    print(f"{celsius}°C is {fahrenheit}°F")

temperature = float(input("Enter the temperature to convert:"))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()
if unit== "C":
    print(convert_to_celsius(fahrenheit=temperature))
elif unit=="F":
    print(convert_to_fahrenheit(celsius=temperature))
else:
    print("enter valid unit and temperature")