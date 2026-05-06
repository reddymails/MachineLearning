####
#

# Example enter 23
n = input("Enter  Your input  String or int or float:")
print("You entered " + n)
print(" Data type="+ str(type(n)))

n = int(n)
print(" Value ="+ str(n))
print(" Data type after conversion ="+ str(type(n)))

if n%2 == 0:
    print("The number is even")
else:
    print("The number is odd")

if 4 > 2 and 3*4 == 12:
    print(" Used and exoression ")
    print(" You dont need curly braces")
else:
    print("The number is even")

# Will add .0 to 23 if you entered 23. So output will be 23.0
n = float(n)
print(" Value ="+ str(n))
print(" Data type after conversion ="+ str(type(n)))


dish =  input(" Enter your favourite dish")
indian = ["Rice","Jamoon","Roti"]
chinese = ["Noodles","Egg role","Fried Rice"]
italian = ["pizza","pasta","risotto"]

if dish in indian:
    print("The dish is indian")
elif dish in chinese:
    print("The dish is chinese")
elif dish in italian:
    print("The dish is italian")
else :
    print("The dish is not in the list")

