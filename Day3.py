#Declaring variables
name= 'Eman'
print(name)

x= 4
#We can change type of variables after they have been set.
x= 'a'
print(type(x))

#String variables can be declared either by using single or double quotes.
x= 'a'
x= "a"

#Assign the same value to multiple variables in one line.
x = y = z = 'The same value of the three variables'
print(x)
print(y)
print(z)

#To combine both text and a variable, Python uses the + character.
x= 'awesome'
print('Python is '+x)

# + used also to add a variable to another variable.
x= 'Python is '
y= 'awesome'
print(x+y)