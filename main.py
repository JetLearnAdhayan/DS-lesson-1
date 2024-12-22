import numpy as np

numbers = [1,2,3,4,5,6,7,8,9,10]


print(type(numbers))

numbers_numpy = np.array(numbers)

print(type(numbers_numpy))

a=np.array([1,2,3])

print(a)

#b=np.array([1,2,3],"hi") can't have numbers and text in an array, you can only have have the numbers data type
#print(b)

c=np.array([7,10,66,9,12])
c=c+10
print(c)

d = np.array([1,45,6,7,9])
d=d*10
print(d)

e=np.zeros(7)
print(e)

f = np.ones(7)
print(f)

g=np.array([23,61,52,241,34], dtype = "float") #float is decimals
print(g)

h=np.array([[1,2,3,4,5],[3,4,5,6,2]])
print(h)

#i=np.array([[1,23,4,5],[123,36,78,23,245]]) 2d array should always have equal numbers on both of the list
#print(i)

print("array dimension: ", h.ndim)#1d 2d 3d
print("number of rows_col: ",h.shape)#number of and colums
print("number of elements: ",h.size)#number of elements
print("Array size: ",h.nbytes)#size in bytes - 4bytes

num_array = np.arange(1,101)#writes all the numbers for example 1-100
print(num_array)

even_array = np.arange(0,101,2)
print(even_array)

odd_array = np.arange(1,101,2)
print(odd_array)

#print numbers in random order:
random_arr = np.random.permutation(np.arange(1,11))
print("Random Order(permutation):" ,random_arr)

random_arr2 = np.random.randint(1,101)
print(random_arr2)

#prints random value from 0-1
random_array = np.random.rand(1,20)
print(random_array)

random3 = np.arange(1,26).reshape(5,5)
print(random3)

random4 = np.arange(1,37).reshape(6,6)
random5 = np.arange(1,37).reshape(2,18)
random6 = np.arange(1,37).reshape(3,12)
random7 = np.arange(1,37).reshape(4,9)
print(random4)
print(random5)
print(random6)
print(random7)

random_arr3 = np.random.permutation(np.arange(1,21))
print(random_arr3)

#sort random numbers:
sorted_array = np.sort(random_arr3)
print(sorted_array)