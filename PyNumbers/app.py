import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(type(array))
print(array.shape)
print(np.zeros((3, 4), dtype=int))

print(np.ones((3, 4), dtype=int))

print(np.full((3, 4), 5, dtype=int))
array = np.random.random((3, 4))

#print(np.random.random((3, 4)))
print(array)
print(array[0, 0])
print(array > 0.2)

print(array[array > 0.2])
print(np.sum(array))
print(np.floor(array))

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
third = first+second
print(third)
print(third+2)

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)
