#
# Class to teach string examples.
#
#

# Simple String concatenation

first = "Ram"
last = "Chandra"

name = first +" "+ last
print(name)

#Stirng formatting .
name = f' { first +" "+ last} is healthy'
print("Formatted String ="+ name)
#Will print 5th char as it's stored as array of characters
print(name[5])
#Prints all characters from 5th position onwards.
print(name[5:])
#prints characters in range.
print(name[5:10])
print(len(name))

#Starting from last char will come 6 characters back
print(name[-7:])

my_food = "Fruits, Salads, Vegetables, egg, Chicken"
# will print false
print("meat" in my_food )
# will print true
print("egg" in my_food )
# will print false
print("egg" not in my_food )

# Multi line.
code_comments = '''
                Oh this multiline is possible 
                when we use tripple quotes.\n       Java copied from python.
'''
print(code_comments)

str_replace = "I need to loose 3kgs before my next race. hope it Works"
str_replace = str_replace.replace("3kgs","3.5 Kgs")
print(str_replace)

# To print all functions supported by String use dir method
print(dir(str_replace))

print(str_replace.upper())
print(str_replace.lower())
print(str_replace.capitalize())
print(str_replace.title())

age = 18
str_format = f'My age is {age} years'
print(str_format)

length = '30 cm'
width = '40 cm'
rectangle = f' The rectangle is \n {length}  in length \n {width}  and width'
print(rectangle)





