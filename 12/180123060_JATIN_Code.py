""" Lab-12
    
    !! Designed by Jatin Dhingra !!
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['agg.path.chunksize'] = 10000

def decimalToBinary(n):  
    return bin(n).replace("0b", "")

def decimalToTernary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

# Part 1
print("First 25 values of the Van der Corupt sequence, using the radical inverse function are as follows")
for i in range(0, 25):
    s= decimalToBinary(i)
    value= 0
    for j in range(0, len(s)):
        if s[len(s)-j-1]=='1':
            value+= 1.00/pow(2, j+1)
    print(value)



Values= []
for i in range(0, 100000):
    s= decimalToBinary(i)
    value= 0
    for j in range(0, len(s)):
        if s[len(s)-j-1]=='1':
            value+= 1.00/pow(2, j+1)
    Values.append(value)
XAxis= []
YAxis= []
for i in range(0, 999):
    XAxis.append(Values[i])
for i in range(1, 1000):
    YAxis.append(Values[i])
plt.scatter(XAxis,YAxis)
plt.xlabel("x(i)",size= 20)
plt.ylabel("x(i+1)",size= 20)
plt.title("Graph between x(i) and x(i+1).. Used radical inverse method",size= 20)
plt.show()



N= [100, 100000]
for n in N:
    UsingRadical= []
    Using_LCG= []
    for i in range(0, n):
        UsingRadical.append(Values[i])
    m= 244944
    a= 1597
    b= 51749
    x0= 1
    for i in range(0, n):
        x= (a*x0 + b)%m
        Using_LCG.append((x*1.000)/(m*1.000))
        x0= x
    plt.hist(UsingRadical, bins = 100, rwidth = 0.5)
    plt.xlabel('Value',size= 20)
    plt.ylabel('Frequemcy',size= 20)
    plt.title('Plotting Distribution Using Radical Inverse method',size= 20)
    plt.legend()
    plt.show()

    plt.hist(Using_LCG, bins = 100, rwidth = 0.5)
    plt.xlabel('Value',size= 20)
    plt.ylabel('Frequemcy',size= 20)
    plt.title('Plotting Distribution Using LCG',size= 20)
    plt.legend()
    plt.show()


# Part 2
ValuesInTernary= []
for i in range(0, 100000):
    s= decimalToTernary(i)
    value= 0
    for j in range(0, len(s)):
        if s[len(s)-j-1]=='1':
            value+= 1.00/pow(3, j+1)
        if s[len(s)-j-1]=='2':
            value+= 2.00/pow(3, j+1)
    ValuesInTernary.append(value)

for n in N:
    XAxis= []
    YAxis= []
    for i in range(0, n):
        XAxis.append(Values[i])
        YAxis.append(ValuesInTernary[i])
    print(n)
    plt.plot(XAxis,YAxis)
    plt.xlabel("Phi2(i)",size= 20)
    plt.ylabel("Phi3(i)",size= 20)
    plt.title("Generating x[i] using Halton sequence in 2-D",size= 20)
    plt.show()


