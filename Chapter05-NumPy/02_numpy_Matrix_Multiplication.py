import numpy as np

q1 = np.array([
    [200, 220, 250],  # Product A
    [150, 180, 210],  # Product B
    [300, 330, 360]   # Product C
])

q2 = np.array([
    [209, 231, 259],  # Product A
    [155, 192, 222],  # Product B
    [310, 340, 375]   # Product C
])

print(q1+q2)


prices = np.array([
    [10, 11, 12],  # Product A
    [8, 9, 10],  # Product B
    [21, 22, 8]   # Product C
])

q1_revenue = q1 * prices

print('q1_revenue=' + str(q1_revenue))
q1_discount  = q1 * 0.2

print('q1_discount=' + str(q1_discount))

q1_net_revenue = q1_revenue - q1_discount

print("q1_net_revenue="+ str(q1_net_revenue))



# horizontal stacking .. almost like a SQL join  on array
name_id_array = np.array([
    [100, 'Ramachandra'],
    [101, 'Rob'],
    [102, 'Raja'],
])

name_salary_and_date_array = np.array([
    [100, 100000,'03-17-2026'],
    [101, 990000,'03-18-2026'],
    [101, 960000,'03-17-2026'],
])

combined_salary_name = np.hstack((name_id_array, name_salary_and_date_array))
print(combined_salary_name)

# whn splitting tell how many columns you want in first array
a, b =  np.hsplit(combined_salary_name,[2])
# we got original uncombined arrays back.
print('a=' + str(a))
print('b='+ str(b))

# Vertical split.
c, d =  np.hsplit(combined_salary_name,[3])
print('c='+ str(c))
print('d='+ str(d))


monthly_sales = np.array([31,33,34,36])
result =  monthly_sales > 33
print('result='+ str(result))

max_args = np.argmax(monthly_sales)
print(' Max='+str(max_args))

print(' Last Element='+ str(monthly_sales[max_args]))










