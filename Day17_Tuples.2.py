# Check if item exists
thistuple = ("apple", "banana", "cherry")
if 'apple' in thistuple:
    print("Yes,'apple' is in the fruits tuple")
	
# Repeating items in the tuple
tuple_1 = ("Python",) * 3
print(tuple_1) #('Python', 'Python', 'Python')

# Tuple length
print(len(thistuple)) #3

# converting list to tuple
my_list= [1,2,3,4,5]
my_list= tuple(my_list)
print(type(my_list)) #<class 'tuple'>