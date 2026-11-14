# 3.1 ----------------
company = "ABC Data" 
phone = "555-123-009" 
employees = 25 
remote_work = True 
big_company = employees > 100 
income = 4500000 
income_per_person = income / employees

 7 zmiennych: 
company - string, value: "ABC Data"
phone - string, value: "555-123-009"
employees - int, value: 25
remote_work - bool, value: True
big_company - bool, value: False
income - int, value: 4500000
income_per_person - float, value: 180000.0
# 3.2 ----------------
###
# A program that calculates the sum of two numbers.
# Modify the program to calculate the sum of three numbers.
#
number1 = 71
number2 = 14
number3 = 48 # trzecia liczba
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3) # print trzeciej liczby
print('The result of summation: ', result)
# 3.3 ----------------
###
# A program for swapping two variable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)
# 3.4 ----------------
###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70
speed_ms = speed_kmh * 1000 / 3600  # mnozenie kilometrow przez 1000 i dzielenie przez 3600 tyle, ile ma godzina
print(speed_kmh, "km/h = ", speed_ms, "m/s")
# 3.5 ----------------
###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8 
przekatna = math.sqrt(a**2 + b**2) # wzór na przekątną prostokąta
print("Dlugosc przekatnej wynosi:", przekatna) # wyswietlenie dlugosci przekatnej
# 3.6 ----------------
# program , który oblicza dystans obserwatora od obiektu, znając jego wysokość
import math
h = float(input("Podaj wysokosc obiektu w metrach: "))
d = 3.57 * sqrt(h) # wzor na dystans obserwatora od obiektu w kilometrach
print("Dystans obserwatora od obiektu wynosi: ", d, "m")
# I. 
h = 1 
d = 3.57 * sqrt(1) = 3.57 km
# II. 
h = 20
d = 3.57 * sqrt(20) = 15.98 km
# 3.7 ----------------
###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere: ", south) # liczba ludzi w polkuli poludniowej
print("Southern Hemisphere in %: ", south/total*100) # procent ludzi w polkuli poludniowej
# 3.8 ----------------
###
# A program that calculates and prints
# the average grade of a student
#
math = 5
art = 4
music = 5
history = 3 # zmiana ze stringa na int
average = math + art + music + history / 4 # poprawa literowek i zamiana znaku odejmowania na dodawane
print("Average grade is", average) # zamiana ' na " oraz poprawa literowki