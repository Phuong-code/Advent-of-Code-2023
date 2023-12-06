def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temperatures_fahrenheit = [32, 64, 100, 212]

temperatures_celsius = map(fahrenheit_to_celsius, temperatures_fahrenheit)

print(temperatures_celsius)
