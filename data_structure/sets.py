# cannot be accessed using index first[0] cant be accessible (unordered collection of items)

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
# second.add(5)
# second.remove(5)
len(second)
print(first)  # {1, 2, 3, 4}

# union of two sets
union = first | second
print(union)  # {1, 2, 3, 4, 5}

# intersection of two sets
intersection = first & second
print(intersection)  # {1}

# difference of two sets
diff = first - second
print(diff)  # {2,3,4}

# sematic difference of two sets
diff = first ^ second
print(diff)  # {2,3,4,5}
