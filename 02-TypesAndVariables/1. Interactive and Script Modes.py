# 1.2 ------------------------------------
7 + 4
(30 + 10) / 2
2 ** 3
7 > 5
r = 4
area = 3.14159 * r * r
area
round(area,2) # <- zaokrąglenie do 2 miejsc po przecinku
first_name = "Mary"
last_name = "Brown"
full_name = first_name + ' ' + last_name # <- dodanie spacji między imieniem a nazwiskiem
full_name
print(full_name)
len(full_name) # <- policzenie długości stringa
a = 5
h = 4
pole = (a * h) / 2
print(pole)
num1 = 7
num2  = 12
num3 = 31
srednia = (num1 + num2 + num3) / 3
print(srednia)
# 1.3 ------------------------------------
###
# BMI Calculator
#
height = input('Enter your height in cm: ') # <- input uzytkownika w postaci stringa
weight = input('Enter your weight in kg: ') # <- input uzytkownika w postaci stringa
height = int(height) # <- zamiana stringa na int
weight = int(weight) # <- zamiana stringa na int
bmi = weight / (height/100)**2 # <- wzór na BMI
bmi = round(bmi,2) # <- zaokrąglenie do 2 miejsc po przecinku
print('Your BMI is', bmi) # <- wynik
print('Check on the Internet if your BMI is ok!!')
# 1.4 ------------------------------------
###
# The program simulates five dice rolls.
#
import random # <- import modułu random z pesudolosowymi liczbami
print("Dice rolling simulator")
for i in range(5): # <- petla for, która wykona się 5 razy
    dice_roll = random.randint(1,6) # <- losowanie liczby z przedziału od 1 do 6
    print(dice_roll, end=" ") # <- wypisanie wylosowanej liczby