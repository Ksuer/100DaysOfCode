# Logical operators are used to combine conditional statements.
x= 5
print(x>3 and x<4) #False
print(x>3 or x>4)  #True

# Identity operators are used to compare the objects, if they are actually the same object 
#(with the same memory location)
x= ['apple', 'banana']
y= ['apple', 'banana']
z=x

print(z is not x) #False
print(x is not y) #True

# Membership operators are used to test if a sequence is presented in an object.
x= ['apple', 'banana']
print('banana' in x) #True

# Bitwise operators are used to compare (binary) numbers.
print(~4) #binary representation of 4 is: 100
          # ~ inverts all bits. The result will be 011 (which is: -5)