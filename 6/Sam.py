from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import random
import numpy as np
import math

A= [-0.5, 0, 0.5, 1]
Expectation= np.array([[5], [8]])

Z= []
for i in range(0, 1000):
    while(1):
        U1= random.random()
        U2= random.random()
        U1= 2*U1-1
        U2= 2*U2-1
        X= pow(U1,2)+pow(U2,2)
        if X<=1:
            break
    Y= math.sqrt(-2.0*math.log(X)/X)
    Z1= U1*Y
    Z2= U2*Y
    Z.append([Z1, Z2])

for a in A:
    X= []

    Variance_Covariance= np.array([[1, 2*a], [2*a, 4]])
    Sigma1= math.sqrt(Variance_Covariance[0][0])
    Sigma2= math.sqrt(Variance_Covariance[1][1])
    Raw= (Variance_Covariance[0][1]*1.00)/(Sigma1*Sigma2*1.00)

    x1= []
    x2= []
    for i in Z:
        x1.append(Expectation[0][0] + i[0]*Sigma1)
        t= 1.0-math.pow(Raw, 2)
        p= (i[1]*math.sqrt(t*Sigma2))
        x2.append(Expectation[1][0]+ (Raw*Sigma2*i[0]) + p)
    X= np.array([x1, x2])
    

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    hist, xedges, yedges = np.histogram2d(x1, x2, bins=25, range=[[-1, 10], [-1, 10]])
    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0
    dx = dy = 0.5 * np.ones_like(zpos)
    dz = hist.ravel()
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Frequency')
    plt.title("Generating Random Number X= [X1, X2] for a= "+str(a))
    plt.show()
    
    X1= x1
    X2= x2

    if a!=1:
        x1, x2= np.meshgrid(xedges, yedges)
        pos = np.empty(x1.shape + (2,))
        pos[:, :, 0] = x1; pos[:, :, 1] = x2
        rv = multivariate_normal([5, 8], Variance_Covariance)
        fig = plt.figure()
        Final= np.array(rv.pdf(pos))
        Final= (Final*np.amax(hist))/np.amax(rv.pdf(pos))
        ax = fig.gca(projection='3d')
        ax.plot_surface(x1, x2, Final,linewidth=0)
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('f(x1,x2)')
        plt.title("Actual Density f(x1,x2) plotted against (x1 on x axis, x2 on y axis) using inbuilt function for a= "+str(a))
        plt.show()
        
        
        pos = np.empty(x1.shape + (2,))
        pos[:, :, 0] = x1; pos[:, :, 1] = x2
        phi= []
        fig = plt.figure()
        Inverse= np.linalg.inv(Variance_Covariance)
        Determinant= Variance_Covariance[0][0]*Variance_Covariance[1][1] - Variance_Covariance[0][1]*Variance_Covariance[1][0] 
        for i in range(0, len(x1)):
            f= []
            for j in range(0, len(x1[i])):
                X= np.array([[x1[i][j]],[x2[i][j]]]) - Expectation
                Transpose= X.transpose()
                f.append((1.00/math.sqrt(2*math.pi*Determinant))*(math.exp(-0.500*np.dot(np.dot(Transpose,Variance_Covariance),X))))
            phi.append(f)
        phi= np.array(phi)
        ax = fig.gca(projection='3d')
        ax.plot_surface(x1, x2, phi,linewidth=0)
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('f(x1,x2)')
        plt.title("Simulated Density f(x1,x2) plotted against (x1 on x axis, x2 on y axis) using Phi(x1,x2)(Given in Lectures) for a= "+str(a))
        plt.show()

    x1, x2, x3= plt.hist(X1, bins = 100, rwidth = 0.5, label= "Obtained density")
    y= []
    c= (1/math.sqrt(2.00*math.pi*Sigma1*Sigma1))*pow(math.e,(-1*0*0)/(2.0*Sigma1*Sigma1))
    for x in x2:
        F= (1/math.sqrt(2.00*math.pi*Sigma1*Sigma1))*pow(math.e,(-1*(x-Expectation[0][0])*(x-Expectation[0][0]))/(2.0*Sigma1*Sigma1))
        y.append((F*max(x1))/c)
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
        F= (1/math.sqrt(2.00*math.pi*Sigma2*Sigma2))*pow(math.e,(-1*(x-Expectation[1][0])*(x-Expectation[1][0]))/(2.0*Sigma2*Sigma2))
        y.append((F*max(x1))/c)
    plt.plot(x2,y, label= "Actual Density")
    plt.xlabel("Random Value generated(X2)", size=20)
    plt.ylabel("Frequency", size=20)
    plt.title("Marginal Density of X2", size=20)
    plt.legend()
    plt.show()

        