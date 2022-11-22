for i in range(1, 20):
    if i % 4 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 4 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)