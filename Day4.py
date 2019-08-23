#Python numbers
x= 1
y=2.5
z= 1j

#To verify the type of the above variables
print(type(x))
print(type(y))
print(type(z))

#We can convert from one type to another with the int(), float(), and complex() methods
a= float(x)
b= int(y)
c= complex(x)

print(type(a))
print(type(b))
print(type(c))

#Random Numbers
import random
print(random.randrange(1,10))