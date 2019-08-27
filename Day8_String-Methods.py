#strip(): removes any whitespace from the beginning or the end of string
a= ' Hello World '
print(a.strip()) #returns 'Hello World'

#len(): returns the length of a string.
print(len(a)) #returns 13

#lower(): returns the string in lower case.
print(a.lower())

#upper(): returns the string in upper case.
print(a.upper())

#replace(): replaces a string with another string.
print(a.replace('World', 'Eman'))

#split(): splits the string into substrings if it finds instances of the separator.
print('Hello, World'.split(',')) #returns ['Hello', ' World']