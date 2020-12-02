""" Lab-08
    
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
X_at_0= math.exp(S_at_0)

lamda= [0.01, 0.05, 0.1, 0.2]

for Lamda in lamda:
    T= []
    S= []
    for t in range(1, 1001):
        N= np.random.poisson(Lamda*t)
        M= 0
        for i in range(0, N):
            M= M+Normal(Drift, Diffusion)
        Z= Normal(0, 1)
        s= S_at_0 * math.exp((t*(Drift-math.pow(Diffusion, 2)/2.00)) + (Diffusion*math.sqrt(t)*Z)) * math.exp(M)
        S.append(s)
        T.append(t)

    plt.plot(T,S)
    plt.xlabel("Time with t=0 as 30 September, 2020")
    plt.ylabel("Expected Value of Stock")
    plt.title("Using Jump-Diffusion Process with Lambda= "+str(Lamda))
    plt.show()

