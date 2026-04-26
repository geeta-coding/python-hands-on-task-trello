# print(__name__)


# Import the math module and use sqrt, pi, ceil
import math as m
print(m.sqrt(3))
print(m.pi)
print(m.ceil(12))



# Import specific functions: from random import randint
import random as r
print(r.randint(1,10))



# Use alias: import numpy as np (concept)
# Create your own module: myutils.py with helper functions

import main_day_16 as a
num = int(input("enter the 1 st number : "))
num_2 = int(input("enter the number 2 : "))

a.add(num,num_2)
a.sub(num,num_2)

# Import your module in another script


# Understand name == 'main' guard
print(__name__)


# Explore dir() to see what's inside a module
print(dir())


# Use the os, sys, datetime modules for basic tasks
from datetime import datetime

now = datetime.now()
print(now)

print(now.date())        
print(now.time())        
import os

print(os.getcwd())       
print(os.listdir())       
import sys

print(sys.version)     
print(sys.argv)        