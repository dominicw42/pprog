# 4.1 -------------------
###
# Printing student's personal data
#
name = "Adam"
age = 20
height = 178
age2 = age + 6
print(f"My name is {name}. I am {age} years old and my height is {height} cm.")
print(f"In 6 years I will be {age2} years old.")
# 4.2 -------------------
###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members
print(f'Total family income is {total_income}, and income per person is {income_per_person}')
# 4.3 -------------------
a = 3
b = 5
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')