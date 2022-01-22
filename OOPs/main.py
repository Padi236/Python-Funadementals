#since math module come directly while installing python it is imported directly



import math as m            #You can rename a module while importing
import Calculator
import sys

print(sys.path)
print(sys.modules)

print(m.sqrt(25))

print(__name__)

print(m.pi)
print(m.sin(0.79))

## To import a specific definition like a constant or a function
## for single func   : from math import sqrt
## For multiple func : from math import sqrt, pi, sin
## for all           : from math import *     (Bad coding practice)

#To display all the function in maths module
print(dir(m))

print(Calculator.add(23,4))
print(Calculator.subtract(23,4))
print(Calculator.multiply(23,4))
print(Calculator.divide(23,4))