

str1= "Please, I want {} sandwishes and {} donutes"
#change 'I' to 'We'
#fill {} with 7 and 5
#capitalize each 'a' letter in the sentence

str1= str1.replace('I', 'We').replace('a', 'a'.capitalize()).format(5,7)

print(str1) #PleAse, We wAnt 5 sAndwishes And 7 donutes
