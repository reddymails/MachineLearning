#
# Create a list of your friends' names and now create a list of tuples. The tuple should contain the friend’s name and
# the length of the name. For Example: if someone’s name is Aditya, the tuple would be: (‘Aditya’, 6)

#contacts = [('Ram',9854666),('Raja',89765455),('Rob',8976543)]

import numpy as np


friends_tuple = [('Adithya', 6),('Ram',3),('Raja',4)]
print(friends_tuple)
print(friends_tuple[0])


# You and your wife argued about expenses last night. You both want to know who is spending more in a month.
# Now you both go to the Little Yoda he is a good python programmer. He suggested that both of you add an entry in a
# dictionary next time you spend money. So that you can have a clear picture of your expenses and plan to reduce them. Both dictionaries are as below-

husband_expenses = {'Clothes':1100,'Shoes':1000,'Watch':900 ,'Mobile Recharge':699 ,'Petrol':1980}
wife_expenses = {'Clothes':2310,'Shoes':999,'Makeup':3670 ,'Mobile Recharge':799 ,'DTH recharge':999}

husband_sum =0
highest_husband = 0
highest_husband_category =''
for key in husband_expenses.keys():
    husband_sum += husband_expenses.get(key)
    if(highest_husband < husband_expenses.get(key)):
        highest_husband = husband_expenses.get(key)
        highest_husband_category = key

wife_sum =0
highest_wife = 0
highest_wife_category =''
for key in wife_expenses.keys():
    wife_sum += wife_expenses.get(key)
    if (highest_wife < wife_expenses.get(key)):
        highest_wife = wife_expenses.get(key)
        highest_wife_category  = key

print('highest_husband='+ str(highest_husband) +" highest_husband_category="+ highest_husband_category)
print('highest_wife=' + str(highest_wife)+" highest_wife_category="+ highest_wife_category)


print('Husband ='+ str(husband_sum))
print('Wife ='+ str(wife_sum))
if(husband_sum > wife_sum):
    print('husband sum is greater than wife.')
else:
    print('Wife sum is Greater than husband sum.')

print(dir(np))



