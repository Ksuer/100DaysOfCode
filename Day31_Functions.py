# Creating a Function
def my_function():
    print('Hello World')
    
my_function()

# Default Parameter Value
def my_function(city='Riyadh'):
    print('I live in', city)

#If we call the function without parameter, it uses the default value.
my_function()
my_function('Jeddah')