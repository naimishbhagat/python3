print("Hello World")
print("*" * 10)
print("Hello")
x = 1


def fizz_buz(num):
    if(num % 3 == 0 and num % 5 == 0):
        return 'FizzBuzz'
    if(num % 3 == 0):
        return 'Fizz'
    if(num % 5 == 0):
        return 'Buzz'

    return num


print(fizz_buz(15))
