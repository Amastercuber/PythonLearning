#!/bin/python
#https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    print ("Enter an integer: ")
    n = int(input().strip())
if not (n>= 1 and n<=100):
    print ("please enter another number")
    exit()
#If  is odd, print Weird
if (n % 2) == 0 and n >= 2 and n <= 5:
    print("Not Weird")
elif (n % 2) == 0 and n >=6 and n <= 20:
    print("Weird")
#If is even and in the inclusive range of  to , print Not Weird
elif (n % 2) == 0 and n >= 20:
    print("Not Weird")
elif (n % 2) == 1:  
    print ("Weird")