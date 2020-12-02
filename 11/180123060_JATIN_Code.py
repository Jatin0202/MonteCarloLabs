""" Lab-11
    
    !! Designed by Jatin Dhingra !!
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt

N= [10, 20, 50, 100]
U= []

# Generating U from Linear Congruence Generator
m= 244944
a= 1597
b= 51749
x0= 1
for i in range(0, 10000):
    x= (a*x0 + b)%m
    U.append((x*1.000)/(m*1.000))
    x0= x



for n in N:
    Discrepancy= 0
    Volume_A= 1.00/(n*1.00)
    NoOfValuesInInterval= []
    for i in range(0, n):
        NoOfValuesInInterval.append(0)
    for i in range(0, 10000):
        NoOfValuesInInterval[(int)(U[i]*n)]+=1
    for i in range(0, n):
        NoOfValuesInInterval[i]/=10000.00
        Discrepancy= max(Discrepancy, abs(NoOfValuesInInterval[i]-Volume_A))
    
    print("N= %d"%n)
    print("Volume(A)= %f"%Volume_A)
    print("Discrepancy= %f\n\n"%Discrepancy)