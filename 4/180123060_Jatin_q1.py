import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.stats import beta 

# taking alpha1 and alpha2 to be greater than 1 in all cases
alpha1= [2, 5, 10, 15, 20]
alpha2= [8, 9, 10, 11, 12]

# xStar stores value of x where Beta function takes its maximum value
xStar= []
# c stores the value of f(x) at xStar(Using inbuilt Beta function in python)
c= []

# This function accept or reject value of u1(Acception Rejection Method) 
def AcceptReject(f,c):
    u2= random.random()
    if c*u2<=f:
        return 1
    else:
        return 0

for i in range(0,5):
    xStar.append((alpha1[i]*1.00-1.00)/(alpha1[i]*1.00+alpha2[i]*1.00-2.00))
    c.append(beta.pdf(xStar[i], alpha1[i], alpha2[i])) 
    X= []
    iterations= []
    
    for j in range(0,10000):
        count= 0
        while(1):
            u= random.random()
            f= beta.pdf(u, alpha1[i], alpha2[i])
            if AcceptReject(f, c[i]):
                X.append(u)
                count+=1
                break
            else:
                count+=1
                continue
        iterations.append(count)
    
    x1,x2,x3= plt.hist(X, bins = 100, rwidth = 0.5, label= "Obtained density")
    y= []
    for x in x2:
        f= beta.pdf(x, alpha1[i], alpha2[i])
        y.append((f*1.00*max(x1/c[i]))) 
    
    plt.plot(x2,y, label= "Actual Density")
    plt.xlabel("Value", size=20)
    plt.ylabel("Frequency", size=20)
    plt.title("Generating Random Numbers having Beta Distribution using alpha1= "+str(alpha1[i])+"and alpha2= "+str(alpha2[i]), size=20)
    plt.legend()
    plt.show()

# Printing values of alpha1, alpha2, XStar, c(or f(XStar))
print("Alpha1")
print(alpha1)
print("Alpha2")
print(alpha2)
print("XStar")
print(xStar)
print("c")
print(c)


    

    


