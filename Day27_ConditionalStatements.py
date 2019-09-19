# If statement
a=30
b=40
if b>a:
    print('b is greater than a')
	
# Elif
a=30
b=30
if b>a:
    print('b is greater than a')
elif a==b:
    print('a and b are equal')
	
# Else
# The else keyword catches anything which isn't caught by the preceding conditions.
a=50
b=30
if b>a:
    print('b is greater than a')
elif a==b:
    print('a and b are equal')
else:
    print('a is greater than b')
	
# One line if statement
a=50
b=30

if a > b: print('a is greater than b')

# One line if else statement
a=50
b=30

print('A') if a>b else print('B') #result: A

# and: logical operator
a= 200
b= 33
c= 500

if a>b and c>a:
    print('Both conditions are True')
	
# or: logical operator
a= 200
b= 33
c= 500

if a>b or c<a:
    print('At least one of the condition is True')