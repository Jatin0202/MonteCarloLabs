# use python 180123060_Jatin_q1.py to run this code

import matplotlib.pyplot as plt

# initially lets assume a, m to find first 17 values of u 
a= 31
m= 17
u= []
x= 1 # value of x0

# definning function for ploting graph and bar
def plot(u):
    Xaxes= []
    Yaxes= []
    frequency= []
    X= []
    for i in range (0,20):
        frequency.append(0)
        key= str(i*0.05)+"-"+str(i*0.05+0.05)
        X.append(key)

    for i in range(0,len(u)):
        if i==0:
            Xaxes.append(u[i])
        elif i==(len(u)-1):
            Yaxes.append(u[i])
        else:
            Xaxes.append(u[i])
            Yaxes.append(u[i+1])
        frequency[(int)(u[i]*100)/5]+=1

    #plotting graph between u[i] and u[i+1]
    plt.scatter(Xaxes,Yaxes)
    plt.xlabel("u[i]")
    plt.ylabel("u[i+1]")
    plt.title("Graph between u[i] and u[i+1] for no of values %d"%len(u))
    plt.show()

    #plotting bargraph 
    fig = plt.figure(figsize = (10, 5)) 
    plt.bar(X, frequency,  color ='b',width = 0.4) 
                
    plt.legend()
    plt.xlabel("Range of value of u") 
    plt.ylabel("Frequency") 
    plt.title("BarGraph for no of values "+str(len(u))) 
    plt.show()


# finding first 17 value of u
print('First 17 values of u are(using linear congruence)')
for i in range(0,17):
    u.append((x*1.00)/(m*1.00))
    print('u%d ='%i),
    print('%0.4f'%u[i])
    x= (a*x)%m
    
# for 1000 values
for i in range(17,1000):
    U= u[i-17]-u[i-5]
    if U<0:
        U=U+1.00
    u.append(U)
plot(u)

# for 10000 values
for i in range(1000,10000):
    U= u[i-17]-u[i-5]
    if U<0:
        U=U+1.00
    u.append(U)
plot(u)

# for 100000 values
for i in range(10000,100000):
    U= u[i-17]-u[i-5]
    if U<0:
        U=U+1.00
    u.append(U)
plot(u)
