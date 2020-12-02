""" Lab-09
    
    !! Designed by Jatin Dhingra !!
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Given Mean, Variance Generate random number satisfying N(Mean, Variance)
def Normal(Mean, SD):
    U1= random.random()
    U2= random.random()
    R= -2*math.log(U1)
    V= 2*math.pi*U2
    Z1= math.sqrt(R)*math.cos(V)
    return Mean*1.00+Z1*SD

# Using value of Drift Coefficient and Diffusion Coefficient that was calculated iin previous lab
Drift= 0.000298
Diffusion= 0.022282
# Taking value of S(0) at 30 Sept, 2020 as in Lab-07 
S_at_0= 185.399994
T= 30
K= 1.1*S_at_0
M= 1000
N= 300
Payoff= []

for i in range(0, M):
    Payoff.append(0)
    s= 0
    for j in range(0, N):
        Z= Normal(0, 1)
        t= (j+1)*T/N
        s+= S_at_0 * math.exp((t*(Drift-math.pow(Diffusion, 2)/2.00)) + (Diffusion*math.sqrt(t)*Z))
    Payoff[i]= max(0, K-s/N)
Mean= np.average(Payoff)
Variance= np.var(Payoff)
print("     Part 1                   ")
print("     Mean: %f"%Mean)
print("     Variance: %f"%Variance)
print("     95Percent Confidence Interval: [%f, %f]\n\n\n"%(Mean-(1.96*Variance)/math.sqrt(M), Mean+(1.96*Variance)/math.sqrt(M)))


print("     Part 2 (Using Control Variables)                   ")
X= []
for i in range(0, M):
    X.append(0)
    Z= Normal(0, 1)
    s= S_at_0 * math.exp((T*(Drift-math.pow(Diffusion, 2)/2.00)) + (Diffusion*math.sqrt(T)*Z))
    X[i]= max(0, K-s)
Mean_of_X= np.average(X)
b= 0
s= 0
for i in range(0, M):
    b+= (X[i]-Mean_of_X)*(Payoff[i]-Mean)
    s+= pow(X[i]-Mean_of_X, 2)
b= b/s
print("     Value of b: %f"%b)
Y_Using_b= []
for i in range(0, M):
    Y_Using_b.append(Payoff[i]- b*(X[i]-Mean_of_X))
Mean= np.average(Y_Using_b)
Variance= np.var(Y_Using_b)
print("     Mean: %f"%Mean)
print("     Variance: %f"%Variance)
print("     95Percent Confidence Interval: [%f, %f]\n\n\n"%(Mean-(1.96*Variance)/math.sqrt(M), Mean+(1.96*Variance)/math.sqrt(M)))
