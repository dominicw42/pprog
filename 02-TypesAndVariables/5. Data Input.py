# 5.1 -----------------------------------------------
# A program that reads your first and last name from the keyboard.
# Store this data in two separate variables.
# Then, print your full name i.e. first and last name separated by a single space.
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')
# 5.2 -----------------------------------------------
###
# A program to calculate the volume and surface area of ​​a cube.
# 
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
cube_volume = cube_side ** 3
cube_surface_area = 6 * (cube_side ** 2)
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')
# sprawdzenie dzialania dla podanych wartosci
cube_side_string = input('Enter cube side: ')
Enter cube side: 4
cube_side = int(cube_side_string)
cube_volume = cube_side ** 3
cube_surface_area = 6 * (cube_side ** 2)
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
The volume of a cube with side 4 is 64
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')
The surface area of a cube with side 4 is 96

cube_side_string = input('Enter cube side: ')
Enter cube side: 7
cube_side = int(cube_side_string)
cube_volume = cube_side ** 3
cube_surface_area = 6 * (cube_side ** 2)
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
The volume of a cube with side 7 is 343
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')
The surface area of a cube with side 7 is 294
# 5.3 -----------------------------------------------
###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('Length a=')
b = input('Width b=')
c = input('Height c=')
a = int(a)
b = int(b)
c = int(c)
volume = a * b * c
surface_area = 2 * (a * b + a * c + b * c)
print(f'The volume of a cuboid with sides {a}, {b}, and {c} is {volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, and {c} is {surface_area}')
# sprawdzenie dzialania dla podanych wartosci
a = input('Length a=')
Length a=3
b = input('Width b=')

Width b=4
c = input('Height c=')
Height c=5
a = int(a)

b = int(b)
c = int(c)
volume = a * b * c

surface_area = 2 * (a * b + a * c + b * c)

print(f'The volume of a cuboid with sides {a}, {b}, and {c} is {volume}')

The volume of a cuboid with sides 3, 4, and 5 is 60
print(f'The surface area of a cuboid with sides {a}, {b}, and {c} is {surface_area}')

The surface area of a cuboid with sides 3, 4, and 5 is 94

a = input('Length a=')
Length a=8
b = input('Width b=')
Width b=1
c = input('Height c=')
Height c=2
a = int(a)
b = int(b)

c = int(c)
volume = a * b * c
surface_area = 2 * (a * b + a * c + b * c)
print(f'The volume of a cuboid with sides {a}, {b}, and {c} is {volume}')
The volume of a cuboid with sides 8, 1, and 2 is 16
print(f'The surface area of a cuboid with sides {a}, {b}, and {c} is {surface_area}')
The surface area of a cuboid with sides 8, 1, and 2 is 52
# wyniki volume = 94 i surface_area = 60 sa na odwrot

# 5.4 -----------------------------------------------
amount = input('Wpisz kwote w ZL: ')
vat = 0.23
amount = float(amount)
vat_amount = amount * vat
vat_amount = round(vat_amount, 2)
print(f'Kwota wynosi {amount} ZL, a podatek VAT wynosi {vat_amount} ZL')
# sprawdzenie dzialania dla podanych wartosci
amount = input('Wpisz kwote w ZL: ')
Wpisz kwote w ZL: 15.84
vat = 0.23

amount = float(amount)
vat_amount = amount * vat
vat_amount = round(vat_amount, 2)
print(f'Kwota wynosi {amount} ZL, a podatek VAT wynosi {vat_amount} ZL')
Kwota wynosi 15.84 ZL, a podatek VAT wynosi 3.64 ZL
# 5.5 -----------------------------------------------
regular_price = float(input('Enter price:'))
discount = int(input('Enter discount %: '))
discounted_price = regular_price * (discount / 100)
reduction = regular_price - discounted_price
regular_price = round(regular_price, 2)
discounted_price = round(discounted_price, 2)
reduction = round(reduction, 2)
print(f'Price without discount: {regular_price}')
print(f'Price with discount: {discounted_price}')
print(f'Reduction: {reduction}')
