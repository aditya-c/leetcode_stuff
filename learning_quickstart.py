celsius = [37, 39.2, 36.5, 37.8]
fahrenheit = map(lambda x: (float(5) / 9) * x + 32, celsius)
print(fahrenheit)
