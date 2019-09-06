# Creating tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# The data inside a tuple can be of one or more data types.
my_tuple = ("Ahmed", 1.1, 2)
print(my_tuple)

# We can access tuple items by referring to the index number, inside square brackets []
print(thistuple[1]) #banana

# Loop through a tuple
for x in thistuple:
    print(x)
	
# Tuple slicing
print(thistuple[0:2]) #('apple', 'banana')