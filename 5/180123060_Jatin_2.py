import matplotlib.pyplot as plt
import random
import numpy as np
import math
import time

# Z contains random numbers generated using Marsaglia and Bray Method corresponding to N(0,1)
Z= []
NoOfValues= [100, 10000]
Mean= []
Variance= []
Time= []
NoOfAcceptedValues= []
NoOfRejectedValues= []

for j in NoOfValues:

    accepted= 0
    rejected= 0
    start= time.time()
    for i in range(0,j//2):
        while(1):
            U1= random.random()
            U2= random.random()
            U1= 2*U1-1
            U2= 2*U2-1
            X= pow(U1,2)+pow(U2,2)
            if X<=1:
                accepted+=1
                break
            else:
                rejected+=1
        Y= math.sqrt(-2.0*math.log(X)/X)
        Z1= U1*Y
        Z2= U2*Y
        Z.append(Z1)
        Z.append(Z2)
    NoOfAcceptedValues.append(accepted)
    NoOfRejectedValues.append(rejected)
    end= time.time()
    Time.append(end-start)

    mean= sum(Z) / len(Z)
    variance= sum((k - mean) ** 2 for k in Z) / len(Z)
    
    Mean.append(mean)
    Variance.append(variance)
    x1,x2,x3= plt.hist(Z, bins = 100, rwidth = 0.5, label= "Obtained density")
    y= []
    c= (1/math.sqrt(2.00*math.pi))*pow(math.e,(-1*0*0)/2.0)
    for x in x2:
        f= (1/math.sqrt(2.00*math.pi))*pow(math.e,(-1*x*x)/2.0)
        y.append((f*max(x1))/c)
    plt.plot(x2,y, label= "Actual Density")
    plt.xlabel("Random Value generated", size=20)
    plt.ylabel("Frequency", size=20)
    plt.title("Generating Random Numbers using Marsaglia & Bray method method having distribution N(0,1)", size=20)
    plt.legend()
    plt.show()

    
    # Now for N(0,5)
    Z1= []
    for i in Z:
        Z1.append(0+math.sqrt(5)*i)
    x1,x2,x3= plt.hist(Z1, bins = 100, rwidth = 0.5, label= "Obtained density")
    y= []
    c= (1/math.sqrt(2.00*math.pi*5))*pow(math.e,(-1*0*0)/(2.0*5.0))
    for x in x2:
        f= (1/math.sqrt(2.00*math.pi*5))*pow(math.e,(-1*x*x)/(2.0*5.0))
        y.append((f*max(x1))/c)
    plt.plot(x2,y, label= "Actual Density")
    plt.xlabel("Random Value generated", size=20)
    plt.ylabel("Frequency", size=20)
    plt.title("Generating Random Numbers using Marsaglia & Bray method method having distribution N(0,5)", size=20)
    plt.legend()
    plt.show()

    # Now for N(5,5)
    Z2= []
    for i in Z:
        Z2.append(5+math.sqrt(5)*i)
    x1,x2,x3= plt.hist(Z2, bins = 100, rwidth = 0.5, label= "Obtained density")
    y= []
    c= (1/math.sqrt(2.00*math.pi*5))*pow(math.e,(-1*0*0)/(2.0*5.0))
    for x in x2:
        f= (1/math.sqrt(2.00*math.pi*5))*pow(math.e,(-1*(x-5)*(x-5))/(2.0*5.0))
        y.append((f*max(x1))/c)
    plt.plot(x2,y, label= "Actual Density")
    plt.xlabel("Random Value generated", size=20)
    plt.ylabel("Frequency", size=20)
    plt.title("Generating Random Numbers using Marsaglia & Bray method method having distribution N(5,5)", size=20)
    plt.legend()
    plt.show()

print("Mean ", Mean)
print("Variance ", Variance)
print("Time ", Time)
print("\n\n")
print("Proportion of values rejected in both cases(100 and 10,1000 values)")
for j in range(0,2):
    print(NoOfRejectedValues[j]*1.00/(NoOfRejectedValues[j]*1.00+NoOfAcceptedValues[j]*1.00))
print("Actual value of 1-pi/4 : ",1.00-math.pi/4.00)
