# We can combine strings and numbers by using the format() method
str = "This code is written in {}"
print (str.format("Python")) 

# We can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity= 2
item_number= 4
price= 49.5

my_order= 'I want to pay {2} dollars for {0} pieces of item {1}'
print(my_order.format(quantity,item_number,price))