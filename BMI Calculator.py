#!/usr/bin/env python3

# Aiden Henderson
# Palomar College CSIT 175
# Lab 03, Exercise 2
# BMI Calculator

# Variables
height = 0
weight = 0
bmi = 0

# Input
height = int(input("Enter height in inches: "))
weight = int(input("Enter weight in pounds: "))

# Conversions
meters = height / 39.36
kilograms = weight / 2.2
bmi = kilograms / (meters * meters)

# Output
if bmi < 18.5:
    print("Your BMI is: ", int(bmi) ,"Underweight")
elif bmi < 25:
    print("Your BMI is: ", int(bmi) ,"Normal")
elif bmi < 30:
    print("Your BMI is: ", int(bmi), "Overweight")
elif bmi < 35:
    print("Your BMI is: ", int(bmi) , "Obesity Class 1")
elif bmi < 40:
    print("Your BMI is: ", int(bmi) , "Obesity Class 2")
else:
    print("Your BMI is: ", int(bmi) , "Morbid Obesity")


