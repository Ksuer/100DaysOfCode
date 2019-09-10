# Get the length of a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #result: 3

# Removing item form set
# 1. remove() method
thisset.remove("banana")
print(thisset) #{'cherry', 'apple'}

# 2. discard() methhod
thisset.discard("banana")
print(thisset)

# We can also use the pop() method to remove an item
thisset = {"apple", "banana", "cherry"}

# The return value of the pop() method is the removed item.
x = thisset.pop() #cherry

# It is also possible to use the set() constructor to make a set.
thisset = set(("a", "b", "c")) # note the double round-brackets
print(thisset) #{'a', 'c', 'b'}