# -*- coding: utf-8 -*-
"""BodyMassIndexCal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tupg6VkteIKnQrN40Dset7jq3O8g3e2t
"""

#Body Mass Index calculater
def Main():
  Height = float(input("Enter Your Height in Inches: "))
  Weight = float(input("Enter Your Weight in Pounds: "))
  cal(h=Height,w=Weight)



def cal(h,w):
  BMI = (w/(h**2))*703
  print("your BMI is:",BMI)
  if BMI <= 18.4:
    print("You are underweight.")
  elif BMI <= 24.9:
    print("You are healthy.")
  elif BMI <= 29.9:
    print("You are over weight.")
  elif BMI <= 34.9:
    print("You are severely over weight.")
  elif BMI <= 39.9:
    print("You are obese.")
  else:
    print("You are severely obese.")


Main()