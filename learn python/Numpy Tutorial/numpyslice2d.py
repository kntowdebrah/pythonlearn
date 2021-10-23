import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# from the 2nd element return 2nd to the 3rd element
print(arr[1, 1:4])

# from both elements return the 2nd element
print(arr[0:2, 2])

# from both element return the 2nd to the 3rd element(this will be a two dimensional array)
print(arr[0:2, 1:4])

print(arr.dtype)
