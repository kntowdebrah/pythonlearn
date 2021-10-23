import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

print(arr[4:])

print(arr[:4])

print(arr[-3:-1])

# using step every other element from the 2nd to the 4th
print(arr[1:5:2])

# every other element across the whole array
print(arr[::2])
