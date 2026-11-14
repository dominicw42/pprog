# 8.2 ---------------------------------------------
import math
r = float(input("Enter the radius of the circle: "))
pi = math.pi
pi = round(pi, 2)
area = pi * r ** 2
area = round(area, 2)
circumference = 2 * pi * r
circumference = round(circumference, 2)
print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")
# sprawdzenie dzialania
r = float(input("Enter the radius of the circle: "))
Enter the radius of the circle: 1
pi = math.pi
pi = round(pi, 2)
area = pi * r ** 2
area = round(area, 2)
circumference = 2 * pi * r
circumference = round(circumference, 2)
print(f"Area of the circle: {area}")
Area of the circle: 3.14
print(f"Circumference of the circle: {circumference}")
Circumference of the circle: 6.28
#
import math
r = float(input("Enter the radius of the circle: "))
Enter the radius of the circle: 3
pi = math.pi
pi = round(pi, 2)
area = pi * r ** 2
area = round(area, 2)
circumference = 2 * pi * r
circumference = round(circumference, 2)
print(f"Area of the circle: {area}")
Area of the circle: 28.26
print(f"Circumference of the circle: {circumference}")
Circumference of the circle: 18.84
# 8.3 ---------------------------------------------
C = float(input("Enter the temperature in Celsius: ")) # users input in float value
F = (C * 9/5) + 32 # formula for converting Celsius into Fahrenheit
F = round(F, 2) # rounding the value to 2 decimal places
K = C + 273.15
K = round(K, 2)
print(f"Temperature in Fahrenheit: {F}") # printing the outcome in Fahrenheit
print(f"Temperature in Kelvin: {K}") # printing the outcome in Fahrenheit
# 8.4 ---------------------------------------------
###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
inches = round(cm / 2.54)
feet = inches // 12
# calculate the number of feet
inches = inches % 12
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
# 8.5 ---------------------------------------------
###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Input SWIFT code: ')
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')
# sprawdzanie dzialania
swift = input('Input SWIFT code: ')
Input SWIFT code: BPKOPLPW
print(f'Bank Code: {swift[0:4]}')
Bank Code: BPKO
print(f'Country Code: {swift[4:6]}')
Country Code: PL
#
swift = input('Input SWIFT code: ')
Input SWIFT code: CHASUS33
print(f'Bank Code: {swift[0:4]}')
Bank Code: CHAS
print(f'Country Code: {swift[4:6]}')
Country Code: US
#
swift = input('Input SWIFT code: ')
Input SWIFT code: DEUTDEFF
print(f'Bank Code: {swift[0:4]}')
Bank Code: DEUT
print(f'Country Code: {swift[4:6]}')
Country Code: DE
# 8.6 ----------------------------------------------
###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter in Zloty: '))
fuel_consumption = float(input('Enter fuel consumption per 100 km: '))
total_fuel_consumption = (fuel_consumption / 100) * distance
total_cost = fuel_price * total_fuel_consumption
total_cost = round(total_cost, 2)
print(f'The goods are gonna cost {total_cost} Zloty to transport them {distance} km.')
# 8.7 ----------------------------------------------
# Read an integer number from the keyboard
number = int(input('Enter number: '))
binary_num = bin(number)
hex_num = hex(number)
print(f'Binary number: {binary_num}')
print(f'Hexadecimal number: {hex_num}')
