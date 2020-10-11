numbers = [1, 2]
# print(numbers[3])

try:
    with open("app.py") as file:
        print("File opened")
    age = int(input('age:'))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Input is invalid")
else:
    print("No Exceptions")
finally:
    print("Always executed")

# raising exception


def calculate_xfactor(age):
    if(age <= 0):
        raise ValueError("Invalid Input")
    return 10/age


try:
    calculate_xfactor(2)
except ValueError:
    pass
