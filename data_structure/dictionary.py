# collection of key value pair
from sys import getsizeof
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])
# print(point[0]) cannot be access with index
# change value of x
point["x"] = 2
# add value
point["z"] = 3
print(point)  # {'x': 2, 'y': 2, 'z': 3}
if "a" in point:
    print(point["a"])
print(point.get("a", 0))  # None or set 0
del point["x"]
print(point)  # {'y': 2, 'z': 3}
for key in point:
    print(key, point[key])  # y 2, z 3

# another way to iterate
for key, value in point.items():
    print(key, value)  # ('y', 2)('z', 3) touple

values = []
for x in range(5):
    values.append(x * 2)
print(values)  # [0, 2, 4, 6, 8]
values = [x * 2 for x in range(5)]  # list
print(values)  # [0, 2, 4, 6, 8]
values = {x * 2 for x in range(5)}  # set
print(values)  # {0, 2, 4, 6, 8}
values = {x: x * 2 for x in range(5)}  # dictionary
print(values)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# generator expression
values = (x * 2 for x in range(10))  # list
print(values)  # {0, 2, 4, 6, 8}

values = (x * 2 for x in range(100000))  # list
print("gen:", getsizeof(values))  # {0, 2, 4, 6, 8}

# unpacking operator
numbers = [1, 2, 3]
print(*numbers)  # 1 2 3
values = list(range(5))
print(values)  # 1 2 3
values = [*range(5)]
print(values)

# unpack dictionary
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 3}
print(combined)
