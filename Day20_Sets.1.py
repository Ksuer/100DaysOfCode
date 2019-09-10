thisset = {"apple", "banana", "cherry"}
print(thisset) #{'cherry', 'banana', 'apple'}

# We cannot access items in a set by referring to an index, since sets are unordered
# But we can loop through the set items using a for loop
for x in thisset:
    print(x)
	
# Add Items
# 1. To add one item to a set, we use the add() method.
thisset.add("orange")

# 2. To add more than one item to a set, we use the update() method
thisset.update(["mango", "grapes"])

print(thisset) #{'apple', 'mango', 'grapes', 'banana', 'orange', 'cherry'}