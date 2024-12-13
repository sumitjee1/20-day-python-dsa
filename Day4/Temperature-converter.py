#Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp = float(input("Enter the temperature: "))
unit = input("Is this in Celsius or Fahrenheit? (C/F): ").lower()

# Perform the conversion
if unit == 'c':
    print(f"{temp}°C is equal to {celsius_to_fahrenheit(temp)}°F.")
elif unit == 'f':
    print(f"{temp}°F is equal to {fahrenheit_to_celsius(temp)}°C.")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
