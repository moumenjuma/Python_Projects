# -*- coding: utf-8 -*-
"""If_else_Loops .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h61P4hkK7M1xOZ-0n8bNGAuVFzIvMA3w
"""

#Question 1
x1=float(input("What is the length of the Rectangle One? "))
y1=float(input("What is the width of the Rectangle One? "))
x2=float(input("What is the length of the Rectangle Two? "))
y2=float(input("What is the width of the Rectangle Two? "))
r1= x1*y1
r2= x2*y2
if r1>r2:
  print("the area of Rectangle One is greater than the area of Rectangle Two")
elif r1<r2:
  print("the area of Rectangle Two is greater than the area of Rectangle One")
else:
  print("the area Rectangle One is equal to the area of rectangle 2")

#Question 2
g1=float(input("Please enter the amount of gallons of water used this month? "))
if g1>=0 and g1<=3000:
  amount=g1*0.05
  print("You owe",amount)
elif g1>=3001:
  x=g1-3000
  ex=x*0.06
  ow=3000*0.05
  amount=ex+ow
  print("You owe",amount)
else:
  print ("invalid number, print a positive number")

#Question 3
test_score=int(input("Enter your test score ")) #Here user can input any score
if test_score>=90 and test_score<=100: 
    print("GRADE A")
elif test_score>=80 and test_score<=89:
  print("Grade B")
elif test_score>=70 and test_score<=79:
  print("Grade C")
elif test_score>=0 and test_score<=70:
  print("Grade F")
else:
  print("invalid number please print between 0-100")