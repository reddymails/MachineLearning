##########
#  Numoy  (Numeric Python ) usage
#
#
#
###########
import time
#from ctypes.wintypes import SIZE

import numpy as np
import sys
numpy_array = np.array([1,2,3,4,5,6,7,8,9])
print(numpy_array)
print('numpy_array_size='+ str(sys.getsizeof(numpy_array[0]) * len(numpy_array)))


python_list = list(range(10))
print(python_list[:5])

print('python_list='+ str(sys.getsizeof(python_list[0]) * len(python_list)))


#Python
l1 = [1,2,3,4,5,]
l2 = [6,7,8,9,10]
tuplet1= tuple(zip(l1,l2))
print(tuplet1)

for x,y in zip(l1,l2):
    print(x,y)

start_time = time.time()
sum_array = [x+y for x,y in zip(l1,l2)]
print(sum_array)
end_time = time.time()
print("Elapsed time for Python list : ", end_time - start_time)

#Num py
SIZE = 10
n1 = np.arange(SIZE)
n2 = np.arange(SIZE)
print(n1[:SIZE])
print(n2[:SIZE])

start_time = time.time()
n3 = n1 + n2
end_time = time.time()
print("Elapsed time for Numpy list : ", end_time - start_time)

print(n3)

twod_array = np.array ([[10,11,12],[13,14,15]])

twod_array[1,0] = 26
print(twod_array)
print(" Byet size of each element ="+ str(twod_array.itemsize)
      + " Number of elements = " + str(twod_array.size))
print(twod_array)
# Create  n * n matric with  zeros or ones.
print(np.zeros((3,4)))
print(np.ones((3,4)))

print(dir(twod_array))
