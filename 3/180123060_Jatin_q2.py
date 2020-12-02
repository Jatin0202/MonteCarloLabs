# use python 180123060_Jatin_q2.py to run this code

import matplotlib.pyplot as plt
import random
import numpy as np

# function defined which returns bool whether to accept or reject a given random variable
def accept(x,c):
    u= random.random()
    f= 20*x*pow((1-x),3)
    if(u<=f/c):
        return 1
    else:
        return 0

#g(x)= 1 for x in [0,1] for Uniform distribution. Therefore solving f(x)<=cg(x) in [0,1] gives c= 2.109375 
c_val= [2.109375, 5, 10]    # first value is found solving above inequality and others are high value of c as mentioned in part d.
MeanNoOfIterations= []      # Used for storing mean number of iterations in each case.

for c in c_val:
    X= []
    iterations= []
    for i in range(0,100000):
        count= 0
        while(1):
            count += 1
            x= random.random()
            if(accept(x,c)):
                X.append(x)
                iterations.append(count)
                break
    

    x1,x2,x3= plt.hist(X, bins = 100, rwidth = 0.5, label= "Obtained density")
    y= []
    for x in x2:
        f= 20*x*pow((1-x),3)
        y.append(f/(2.109375)*max(x1))

    plt.plot(x2, y, label= "Actual density")
    plt.xlabel('Value',size= 20)
    plt.ylabel('Frequemcy',size= 20)
    plt.title('Generating Random Variables using Acception Rejection Method with c = '+str(c),size= 20)
    plt.legend()
    plt.show()   

    MeanNoOfIterations.append(np.mean(iterations))

print("Value of c      Mean number of iterations")
print("%5f        %f"%(c_val[0],MeanNoOfIterations[0]))
print("%5f        %f"%(c_val[1],MeanNoOfIterations[1]))
print("%5f        %f"%(c_val[2],MeanNoOfIterations[2]))


    
