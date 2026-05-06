
def find_total( expenses):
    '''
    expenses: a list of integers
    :param expenses:
    :return: sum of all numbers in the array.
    '''
    total = 0
    for expense in expenses:
        total += expense
        #print(expense)
    return total

expenses_array = [10, 20, 30, 40, 50]
print(find_total(expenses_array))

# This will print the documentation for the given function.
print(help(find_total))


# I set a default height in case if the value is not sent
def cylinder_volumen(radius, height=5):
    '''
    :param radius:
    :param height:
    :return: pi *r*r* height;
    '''
    return (22/7) * radius *2  * height

print(cylinder_volumen(radius =5))
print(cylinder_volumen(radius =5, height=6))
