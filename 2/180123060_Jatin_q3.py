# use python 180123060_Jatin_q3.py to run this code

import math
import numpy as np
import matplotlib.pyplot as plt

# function for finding variance of list of numbers
def variance(data):
    n = len(data)
    mean = (sum(data)*1.00) / (n*1.00)
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n*1.00
    return variance

Mean= []
Variance= []

# CDF for given function
Y= []
X= np.linspace(0, 1, 10000)
for i in range(0,len(X)):
    Y.append((2.00/math.pi)*math.asin(math.sqrt(X[i])))
MeanForGivenFnc= (sum(X)*1.00)/10000.00
VarianceForGivenFnc= variance(X)

# Defining values of a,c,m for linear congruence function for generating value of U
a= 1597
b= 51749
m= 244944

for i in range(1,5):
    n= pow(10,i+1)
    x0= 1
    u= []
    x= []

    # generating random number using linear congruence function
    for j in range(0,n):
        x0= (a*x0+b)%m
        u.append((x0*1.00)/(m*1.00))
        x.append(pow(math.sin((u[j]*math.pi)/2),2))

    x.sort()
    Mean.append(sum(x)/(n*1.00))
    Variance.append(variance(x))

    min= x[0]
    max= x[len(x)-1]
    Xaxes= []
    YaxesFDF= []
    YaxesCDF= []
    for j in range(0,20):
        l= min+j*(max-min)/20
        r= min+(j+1)*(max-min)/20
        Xaxes.append((l+r)/2)
        YaxesFDF.append(0)
        YaxesCDF.append(0)
        for k in range(0,n):
            if (x[k]>=l) & (x[k]<=r) :
                YaxesFDF[j]+=1
        if j==0:
            YaxesCDF[j]= YaxesFDF[j]
        else:
            YaxesCDF[j]= YaxesFDF[j]+ YaxesCDF[j-1]

    for j in range(0,20):
        YaxesCDF[j]= (YaxesCDF[j]*1.000)/(n*1.00)

    # plotting CDF
    plt.plot(Xaxes,YaxesCDF,label="Obtained")
    plt.plot(X,Y,label="Expected")
    plt.xlabel("x")
    plt.ylabel("F[x]")
    plt.title("Cumulative Distribution Function")
    plt.legend()
    plt.show()

    # plotting FDF
    plt.plot(Xaxes,YaxesFDF)
    plt.xlabel("x")
    plt.ylabel("Frequency")
    plt.title("Frequency Distribution Function")
    plt.show()

#printing Mean and Variance
print("\n\n      Obtained Mean and Variance:")
print("      No. of values     Mean      Variance")
print("      100               %0.2f      %0.4f"%(Mean[0],Variance[0]))
print("      1000              %0.2f      %0.4f"%(Mean[1],Variance[1]))
print("      10000             %0.2f      %0.4f"%(Mean[2],Variance[2]))
print("      100000            %0.2f      %0.4f"%(Mean[3],Variance[3]))


