""" Lab-07
    
    !! Designed by Jatin Dhingra !!
"""

import math
import random

def ReadValueOfStock(S):
    StockFile= open("SBIN.NS.csv", "r+")
    StockFile.readline()
    P= StockFile.readlines()
    for i in P:
        S.append(float(i[44:54]))

# S contain daily stock value(closing)
S= []
U= []
E= 0
Drift= 0
Diffusion= 0

ReadValueOfStock(S)
for i in range(1, len(S)):
    U.append(math.log(S[i]/S[i-1]))
    E= E+U[i-1]
E= E/(len(U)*1.0)
Diffusion= 0
for i in range(0, len(U)):
    Diffusion= Diffusion+math.pow((U[i]-E),2)
Diffusion= Diffusion/(len(U)*1.00-1.00)
Diffusion= math.sqrt(Diffusion)
Drift= E+(math.pow(Diffusion,2))/2.00

print("Value of Drift Coefficient= %f"% Drift)
print("Value of Diffusion Coefficient= %f\n\n"% Diffusion)

print(S[len(S)-1])
T= [7, 14, 21]
for t in T:
    X= []
    for i in range(0,500):
        U1= random.random()
        U2= random.random()
        R= -2*math.log(U1)
        V= 2*math.pi*U2
        Z1= math.sqrt(R)*math.cos(V)
        Z2= math.sqrt(R)*math.sin(V)
        X.append(Z1)
        X.append(Z2)
    

    ApproxValueOfStock= 0
    for i in range(0, 1000):
        ApproxValueOfStock += (S[len(S)-1] * math.exp( ((E) * (t)) + (Diffusion * math.sqrt(t) * X[i]) ))
    ApproxValueOfStock/=1000.00

    if t==7: 
        print("7th October, 2020")
        print("Expected Value: %f"%(ApproxValueOfStock))
        print("Actual Value: 190.70")
        print("Percentage Error: %f%%\n\n"%(((190.70-ApproxValueOfStock)/190.70)*100.00))
    elif t==14:
        print("14th October, 2020")
        print("Expected Value: %f"%(ApproxValueOfStock))
        print("Actual Value: 200.05")
        print("Percentage Error: %f%%\n\n"%(((200.05-ApproxValueOfStock)/200.05)*100.00))
    else:
        print("21th October, 2020")
        print("Expected Value: %f"%(ApproxValueOfStock))
        print("Actual Value: 203.75")
        print("Percentage Error: %f%%\n\n"%(((203.75-ApproxValueOfStock)/203.75)*100.00))

