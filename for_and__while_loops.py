# -*- coding: utf-8 -*-
"""for_and _while_loops.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17v9SAs3aFbmfhG-MZ1aFjlzHONPuw78x
"""

#Question 1
for x in range(1,100):
  if ((x%5)==0):
    if((x%3)==0):
      continue
    print(x)

#Question 2
while (x<=50):
  print(x)
  x=x+1