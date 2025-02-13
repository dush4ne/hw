#!/usr/bin/env python3

# Aiden Henderson
# Palomar College CSIT 175 
# Lab 03, Exercise 3
# Coyote Inn

# import locale
import locale
locale.setlocale(locale.LC_ALL, "en-us")

# Variables
month = 0
nights = 0
price = 0.0

# Input
month = int(input("Enter month (1-12): "))
nights = int(input("Enter number of nights: "))

# Calculations
if month == 1 or month == 2 or month == 3:
    price = 80
elif month == 4 or month == 5 or month == 6:
    price = 90
elif month == 7 or month == 8 or month == 9:
    price = 120
elif month == 10 or month == 11 or month == 12:
    price = 100
else:
    print("Invalid month")

# Output
print("Total Price: ", locale.currency(price * nights, grouping=True))

# Test Data
# Month 6 Nights 4 Expected: 360 Result: 360
# Month 2 Nights 8 Expected: 640 Resuly: 640
# Month 15 Nights 30 Expected: Invalid Month Result: Invalid Month 0
