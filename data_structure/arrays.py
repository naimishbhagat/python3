from array import array
# use array only if you are using large sequence of arrays and if performace issue for other cases use lists and touple
# typecode  need to be same otherwise it will give error
numbers = array("i", [1, 2, 3])
numbers.remove(1)
print(numbers[0])
