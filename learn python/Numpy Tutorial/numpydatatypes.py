import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)


# defining the size
arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

# changing the datatype of the array
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(arr)
print(newarr)
print(newarr.dtype)


# changing the datatype of the array

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
