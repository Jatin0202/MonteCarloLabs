from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import random
import numpy as np
import math
import time

# Given Values of a
ValuesOfA= [-0.5, 0, 0.5, 1]

# E stands for Expectation Matrix and VC stands for Variance-Covariance Matrix
# Initially defining all values in A and VC as 0 (changing in loop)
E= np.array([[5], [8]]) 
VC= np.array([[0, 0], [0, 0]])
A= np.array([[0, 0], [0, 0]])

# First finding 1000 values of Z which has N(0, I2) distribution (using Box- Muller method)
Z1= []
Z2= []
for i in range(0, 1000):
    U1= random.random()
    U2= random.random()
    R= -2*math.log(U1)
    V= 2*math.pi*U2
    z1= math.sqrt(R)*math.cos(V)
    z2= math.sqrt(R)*math.sin(V)
    
    Z1.append(z1)
    Z2.append(z2)

# Now a loop on values in a
for a in ValuesOfA:
    X= []

    VC[0][0]= 1
    VC[0][1]= 2*a
    VC[1][0]= 2*a
    VC[1][1]= 4

    Sigma1= math.sqrt(VC[0][0])
    Sigma2= math.sqrt(VC[1][1])
    Raw= (VC[0][1]*1.00)/(Sigma1*Sigma2*1.00)

    A[0][0]= Sigma1
    A[0][1]= 0
    A[1][0]= Raw*Sigma2
    A[1][1]= math.sqrt(1.0-math.pow(Raw,2))*Sigma2
    
    X1= []
    X2= []
    for i in range(0, 1000):
        x1= E[0][0]+ Z1[i]*A[0][0]
        x2= E[1][0]+ A[1][0]*Z1[i]+ A[1][1]* Z2[i] 
        X1.append(x1)
        X2.append(x2)
    X= np.array([X1, X2])
    

    # Histogram(For problem 2)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    hist, xedges, yedges = np.histogram2d(X1, X2, bins=25, range=[[-1, 10], [-1, 10]])
    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0
    dx = dy = 0.5 * np.ones_like(zpos)
    dz = hist.ravel()
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
    ax.set_xlabel('X1', size=20)
    ax.set_ylabel('X2', size=20)
    ax.set_zlabel('Frequency', size=20)
    plt.title("Generating Random Number X= [X1, X2] for a= "+str(a), size=20)
    plt.show()


    if a!=1:
        # Actual and Simulated
        x1, x2= np.meshgrid(xedges, yedges)
        pos = np.empty(x1.shape + (2,))
        pos[:, :, 0] = x1; pos[:, :, 1] = x2
        rv = multivariate_normal([5, 8], VC)
        fig = plt.figure()
        A= np.array(rv.pdf(pos))
        A= (A*np.amax(hist))/np.amax(rv.pdf(pos))
        ax = fig.gca(projection='3d')
        ax.plot_surface(x1, x2, A,linewidth=0)
        ax.set_xlabel('x1', size=20)
        ax.set_ylabel('x2', size=20)
        ax.set_zlabel('f(x1,x2)', size=20)
        plt.title("Actual Density f(x1,x2) plotted against (x1 on x axis, x2 on y axis) using inbuilt function for a= "+str(a), size= 20)
        plt.show()
        
        pos = np.empty(x1.shape + (2,))
        pos[:, :, 0] = x1; pos[:, :, 1] = x2
        Phi= []
        fig = plt.figure()
        VC_Inverse= np.linalg.inv(VC)
        VC_Determinant= VC[0][0]*VC[1][1] - VC[0][1]*VC[1][0] 
        for i in range(0, len(x1)):
            f= []
            for j in range(0, len(x1[i])):
                X= np.array([[x1[i][j]],[x2[i][j]]]) - E
                X_Transpose= X.transpose()
                f.append((1.00/math.sqrt(2*math.pi*VC_Determinant))*(math.exp(-0.500*np.dot(np.dot(X_Transpose,VC),X))))
            Phi.append(f)
        Phi= np.array(Phi)
        ax = fig.gca(projection='3d')
        ax.plot_surface(x1, x2, Phi,linewidth=0)
        ax.set_xlabel('x1', size=20)
        ax.set_ylabel('x2', size=20)
        ax.set_zlabel('f(x1,x2)', size=20)
        plt.title("Simulated Density f(x1,x2) plotted against (x1 on x axis, x2 on y axis) using Phi(x1,x2)(Given in Lectures) for a= "+str(a), size= 20)
        plt.show()
    

    # Plotting Marginal Density (X1, X2)
    x1, x2, x3= plt.hist(X1, bins = 100, rwidth = 0.5, label= "Obtained density")
    y= []
    c= (1/math.sqrt(2.00*math.pi*Sigma1*Sigma1))*pow(math.e,(-1*0*0)/(2.0*Sigma1*Sigma1))
    for x in x2:
        f= (1/math.sqrt(2.00*math.pi*Sigma1*Sigma1))*pow(math.e,(-1*(x-E[0][0])*(x-E[0][0]))/(2.0*Sigma1*Sigma1))
        y.append((f*max(x1))/c)
    plt.plot(x2,y, label= "Actual Density")
    plt.xlabel("Random Value generated(X1)", size=20)
    plt.ylabel("Frequency", size=20)
    plt.title("Marginal Density of X1", size=20)
    plt.legend()
    plt.show()

    x1, x2, x3= plt.hist(X2, bins = 100, rwidth = 0.5, label= "Obtained density")
    y= []
    c= (1/math.sqrt(2.00*math.pi*Sigma2*Sigma2))*pow(math.e,(-1*0*0)/(2.0*Sigma2*Sigma2))
    for x in x2:
        f= (1/math.sqrt(2.00*math.pi*Sigma2*Sigma2))*pow(math.e,(-1*(x-E[1][0])*(x-E[1][0]))/(2.0*Sigma2*Sigma2))
        y.append((f*max(x1))/c)
    plt.plot(x2,y, label= "Actual Density")
    plt.xlabel("Random Value generated(X2)", size=20)
    plt.ylabel("Frequency", size=20)
    plt.title("Marginal Density of X2", size=20)
    plt.legend()
    plt.show()

print("For a=1, VC matrix is non-singular, Inverse doesnot exist because Determinant value is 0.")
print("Value of Correlation coffecient is 1. which means X1 and X2 are linearly dependent on eanc other.")
