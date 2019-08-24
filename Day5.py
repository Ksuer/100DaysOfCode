x='apple'
y= 'orange'
z= 'limon'

basket= x+y+z 
print(basket) #result: 'appleorangelimon'

basket_list= []
basket_list.append(basket[0:len(x)])
basket_list.append(basket[len(x):(len(basket)-len(z))])
basket_list.append(basket[(len(basket)-len(z)):])
print(basket_list) #result: ['apple', 'orange', 'limon']