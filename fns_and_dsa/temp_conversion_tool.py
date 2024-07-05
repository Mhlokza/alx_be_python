FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temperature=0
def convert_to_celsius(fahrenheit):
    celcius = (temperature-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temperature}°F is {celcius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit= CELSIUS_TO_FAHRENHEIT_FACTOR*temperature+32
    print(f"{temperature}°C is {fahrenheit}°F")

temperature = float(input("Enter the temperature to convert:"))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()
if unit== "C":
    convert_to_celsius(fahrenheit=temperature)
elif unit=="F":
    convert_to_fahrenheit(celsius=temperature)
else:
    print("enter valid unit and temperature")