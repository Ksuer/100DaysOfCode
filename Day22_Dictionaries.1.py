my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(my_dict) #{1: 'a', 2: 'b', 3: 'c'}

# Accessing Items
print(my_dict[1]) #a

# Changing value of item
my_dict[2] = 'd'
print(my_dict) #{1: 'a', 2: 'd', 3: 'c'}

# Loop through dictionary keys
for x in my_dict:
    print(x) # 1 2 3
	
# Loop through dictionary values
for x in my_dict:
    print(my_dict[x]) # a d c
    
# We can also use the values() function to return values of a dictionary.
for x in my_dict.values():
    print(x)
	
# Loop through both keys and values, by using the items() function.
for x,y in my_dict.items():
    print('The key is: {} and the value is: {}'.format(x,y))
    #The key is: 1 and the value is: a
    #The key is: 2 and the value is: d
    #The key is: 3 and the value is: c