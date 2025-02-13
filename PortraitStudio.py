#!/usr/bin/env python3

# Aiden Henderson
# Palomar College CSIT 175
# Lab 03, Exercise 1
# Portrait Studio Service Calculator

# import locale
import locale
locale.setlocale(locale.LC_ALL, "en-us")

# Variables

basePrice = 0.0
dayofWeek = 0
lastName = ""
numSubjects = 0

# Consts

SURCHARGE_PCT = 1.2
SUNDAY = 1
SATURDAY = 7

# input

lastName = input("Enter last name: ")
numSubjects = int(input("Enter number of subjects: "))
dayofWeek = int(input("Enter day of week: (1 for Sunday, 2 for Monday....., 7 for Saturday): "))

# Calculations
if numSubjects == 1:
    basePrice = 100
elif numSubjects == 2:
    basePrice = 130
elif numSubjects == 3:
    basePrice = 150
elif numSubjects == 4:
    basePrice = 165
elif numSubjects == 5:
    basePrice = 175
elif numSubjects == 6:
    basePrice = 180
else:
    basePrice = 185


# Surcharges for Saturday and Sunday
if dayofWeek == SUNDAY or dayofWeek == SATURDAY:
    basePrice = basePrice * SURCHARGE_PCT

# Output
print("Last Name: ", lastName)
print("Total Price: ", locale.currency(basePrice, grouping=True))




















