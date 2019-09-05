# List Length
letters_list= ['a', 'b', 'c', 'd', 'e']
print(len(letters_list)) #5

# Add Item
letters_list.append('f')

# Remove Item
#1- remove(): to remove specified item.
letters_list.remove('d')

#2- pop(): to remove the specified index.
letters_list.pop()

# Make a copy of a list
my_list= letters_list.copy()
print(my_list)

# Make a new list.
numbers_list= list((1,2,3,4,5))
print(numbers_list)

