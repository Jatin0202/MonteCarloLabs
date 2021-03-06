import matplotlib.pyplot as plt

# Defining all the initial values (Taking (a= 1597 & b= 51749) and (a= 51749 & b=0))
m= 244944
a1= 1597
b1= 51749
a2= 51749
b2= 0

#freq1 and freq2 help in making table for frequency in diff range with different seed value
freq1= []
freq2= []

# Looping for 5 different x0(seed value)
for x0 in range(1,6):
    
    #frequency store no of values falling in range (size is 20)
    frequency1= []
    frequency2= []
    for i in range(0,20):
        frequency1.append(0)
        frequency2.append(0)

    #First filling frequency1 (a= 1597)
    x= ((a1*x0)+b1)%m
    while x!=x0:
        u= (x*1.0000)/(m*1.0000)
        frequency1[(int)(u*100)/5]+=1
        x= ((a1*x)+b1)%m

    #Second filling frequency2 (a= 51749)
    x= ((a2*x0)+b2)%m
    while x!=x0:
        u= (x*1.0000)/(m*1.0000)
        frequency2[(int)(u*100)/5]+=1
        x= ((a2*x)+b2)%m

    #plotting bar graph(data1 for a=1597  &  data2 for a=51749)
    Xaxes= []
    for i in range(0,20):
        key= str(i*0.05)+"-"+str(i*0.05+0.05)
        Xaxes.append(key)
    
    fig = plt.figure(figsize = (10, 5)) 
    plt.bar(Xaxes, frequency1, label= 'a= 1597',  color ='b',width = 0.4) 
    plt.bar(Xaxes, frequency2, label= 'a= 51749', color ='r',width = 0.4) 
            
    plt.legend()
    plt.xlabel("Range of value of u= x/m") 
    plt.ylabel("Frequency") 
    plt.title("Value of seed x0= "+str(x0)) 
    plt.show()

    freq1.append(frequency1)
    freq2.append(frequency2)

#making table

print('\n\n\n\n\n\n'),
print('   For a=1597   ')
print('x0'),
for i in range(0,20):
    print('%s '%Xaxes[i]), 
print('\n'),

for i in range(0,5):
    print('%d '%(i+1)),
    for j in range(0,20):
        print('%d    '%freq1[i][j]),
    print('\n'),

print('\n\n\n\n\n\n'),
print('   For a=51749   ')
print('x0'),
for i in range(0,20):
    print('%s '%Xaxes[i]), 
print('\n'),

for i in range(0,5):
    print('%d '%(i+1)),
    for j in range(0,20):
        print('%d       '%freq2[i][j]),
    print('\n'),
