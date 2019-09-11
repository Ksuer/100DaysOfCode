# Dictionary Length
my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(len(my_dict)) #3

# Adding Items
my_dict[4] = 'd'
print(my_dict) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# The pop() method removes the item with the specified key name.
my_dict.pop(4)
print(my_dict) #
{1: 'a', 2: 'b', 3: 'c'}

# The popitem() method removes the last inserted item.
my_dict.popitem()
print(my_dict) #{1: 'a', 2: 'b'}

# The del keyword removes the item with the specified key name.
del my_dict[1]
print(my_dict) #{2: 'b'}