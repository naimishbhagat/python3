from collections import deque
letters = ["a", "b", "c"]
# list of lists
matrix = [[0, 1], [2, 3]]
# lists of 100 0's
zeros = [0] * 100

zeros = [0] * 5
combined = zeros + letters
# merge two lists with +
print(zeros, combined)

# loop 0...20
numbers = list(range(20))
print(numbers)

# loop through string characters
strings = list("Hello world")
print(strings)
print(len(strings))

letters = ["a", "b", "c", "d"]
print(letters[0])  # first item
print(letters[-1])  # last item
# change item
letters[0] = 'e'
print(letters)
# return items between index first 2 items
print(letters[0:2])
# if not specified then it will start from 0 same if end index not specified then it will take total length
print(letters[:2])
print(letters[2:])
print(letters[:])  # will take full list
print(letters[::2])  # will return every 2nd element => result: ['e', 'c']

numbers = list(range(20))
# skip every second element = result [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(numbers[::2])

# unpacking list
numbers = [1, 2, 3]
first, second, third = [1, 2, 3]
print(first, third)

numbers = [1, 2, 3, 4, 4, 5]
first, second, *other = numbers  # other is remaining items
print(first, other)
first,  *other, last = numbers  # other is middle items
print(first, other)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5))

letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter[0], letter[1])
# list unpacking
for key, value in enumerate(letters):
    print(key, value)

# add item

letters = ["a", "b", "c"]
letters.append("d")
print(letters)

# add item to specific index
letters.insert(0, "-")
print(letters)

# remove item
letters.pop()  # last element
print(letters)

letters.pop(0)  # first element
del letters[0:1]
print(letters)

letters.remove("b")  # first "b" element
print(letters)

letters.clear()  # remove whole
print(letters)

# find item
letters = ["a", "b", "c"]
index = letters.index("c")
print(index)
if "d" in letters:
    print(letters.index("d"))
print(letters.count("d"))  # find number of occurances in given list

# sorting list
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
# sort in reverse order
numbers.sort(reverse=True)
print(numbers)

print(sorted(numbers))  # duplicate and create the new list with sorted order

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 10)
]
items.sort()
print(items)

# sort function


def sort_items(item):
    return item[1]


items.sort(key=sort_items)
print(items)

# lambda function
#lambda item:expression
items.sort(key=lambda item: item[1])
print(items)


# map functions
prices = []
for item in items:
    prices.append(item[1])
print(prices)

prices = list(map(lambda item: item[1], items))
print(prices)

# filter function
prices = list(filter(lambda item: item[1] >= 10, items))
print(prices)

# list comprehensions
numbers = [item[1] for item in items]
print(numbers)
# filtered list comprehensions
numbers = [item for item in items if item[1] >= 10]
print(numbers)

# zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]
#[(1, 10), (2, 20), (3, 30)]
combined = zip(list1, list2)
print(list(zip(list1, list2)))

# stacks
# LIFO,FIFO
browsing_session = [1, 2, 3]
browsing_session.append(4)
browsing_session.pop()
if not browsing_session:
    print("Empty")

# Queues
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("Empty")

# Tuple - read only list
point = 1, 2
print(type(point))  # <class 'tuple'>

# concat tuple
point = (1, 2)+(3, 4)
print(point)  # (1, 2, 3, 4)
# repeat a tuple
point = (1, 2) * 3
print(point)  # (1, 2, 1, 2, 1, 2)
# list a tuple
point = tuple([1, 2])
print(point)  # (1, 2)
# access tuple with index
point = (1, 2, 3)
print(point[0:2])  # (1, 2)
# unpack touple
x, y, z = (1, 2, 3)
print(x, y)  # 1, 2

# swapping variable
x = 9
y = 10

x, y = y, x

print(x, y)
