celsius_temps = [0, 10, 20, 30, 40, 50, 60]

fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

print("Fahrenheit temperatures:", fahrenheit_temps)
