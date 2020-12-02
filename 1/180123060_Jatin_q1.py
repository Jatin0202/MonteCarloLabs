m=11
b=0


print("\n\n")
#For a=6
a=6
print("Part A)   For a=6, b=0, m=11   ")

for i in range(0,11):
	print("x%d    "%i),
print('\n'),

for i in range(0,11):
	x= i
	for j in range(0,11):
		u= (x*1.000)/(m*1.000)
		if x==10:
			print('%d    '%x),
		else:
			print('%d     '%x),	
		x= (a*x + b)%m
	print('\n'),
	



print("\n\n")
#For a=6
a=3
print("Part B)   For a=3, b=0, m=11   ")

for i in range(0,11):
	print("x%d    "%i),
print('\n'),

for i in range(0,11):
	x= i
	for j in range(0,11):
		u= (x*1.000)/(m*1.000)
		if x==10:
			print('%d    '%x),
		else:
			print('%d     '%x),	
		x= (a*x + b)%m
	print('\n'),

