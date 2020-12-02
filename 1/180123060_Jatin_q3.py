import matplotlib.pyplot as plt

#defining initial values
a= 1229
b= 1
m= 2048
x0= 1
u= []

#finding x1 and period store period of congurence relation
x= (a*x0 + b)%m
period= 0

#looping for values of x until we get x0
while x!=x0:
    period+=1
    x= (a*x + b)%m
    u.append((x*1.000)/(m*1.000))

#xaxis(u(i-1)) yaxis(u(i))
x= []
y= []
for i in range(0,period-1):
    x.append(u[i])
    y.append(u[i+1])

#plotting points 
plt.scatter(x,y)
plt.xlabel("u(i-1)")
plt.ylabel("u(i)")
plt.title("Graph between u(i-1) and u(i)")
plt.show()