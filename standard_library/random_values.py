import random
import string

print(random.random())
print(random.randint(1, 30))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
# random password
print("".join(random.choices(string.ascii_letters+string.digits, k=4)))
print(string.ascii_letters)
print(string.digits)

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
