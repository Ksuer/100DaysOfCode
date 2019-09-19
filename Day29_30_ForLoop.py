numbers_list= [1,2,3,4,5]

for n in numbers_list:
    print(n)
	
# Looping Through a String
name= 'Eman'
for n in name:
    print(n)
	
# Exit the loop when n is 3
numbers_list= [1,2,3,4,5]

for n in numbers_list:
    if n==3:
        break
    print(n) #1 2
	
# Don't print 3
for n in numbers_list:
    if n==3:
        continue
    print(n) #1 2 4 5
	
# Range function
for x in range(6):
    print(x)
	
for x in range(2,6):
    print(x) #printing numbers from 2 3 4 5