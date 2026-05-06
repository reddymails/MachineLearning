
expenses = [1200,1300,1500,1700]
sum_expenses = sum(expenses)
print('Total using sum function' + str(sum_expenses))

sum = 0
for i, expense in enumerate(expenses):
    print(f' Month {i+1} , Expense: {expense}')
    sum = sum + expense

print('Sum using  for loop:'+ str(sum))


# print 1 to 10, Default starts form 0.
for i in range(3,11):
    print(i)
    if i % 2 == 0 :
        print(" Even ")

n=0
while n <= 10:
        print(n)
        n +=1

for n in range(1, -6, -2):
    print(n, end=', ')



