# Nested Dictionaries
people = {1: {'name': 'a', 'age': '19', 'sex': 'Male'},
          2: {'name': 'b', 'age': '22', 'sex': 'Female'}}

# Make a copy of a dictionary with the copy() method.
my_dict1= people.copy()
print(my_dict1)

# Make a copy of a dictionary with the dict() method.
my_dict2= dict(people)
print(my_dict2)