my_set={1,3,5,7,8}

# Adding 4,8,12 to the set
my_set.update([4,8,12])
print(my_set) #{1, 3, 4, 5, 7, 8, 12}

# Removing 8 from set
my_set.remove(8)
print(my_set) #{1, 3, 4, 5, 7, 12}

my_set.clear()
print(my_set) # set()



my_dict= {'name': 'pigeon', 'type': 'bird', 'skin cover': 'feathers'}
print(my_dict)

print(my_dict['type']) #bird

# Changing value of skin cover
my_dict['skin cover']='new value'
print(my_dict) # {'name': 'pigeon', 'type': 'bird', 'skin cover': 'new value'}