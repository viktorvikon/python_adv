for i in range(1, 101):
    num = ""
    if i % 3 == 0:
        num += "Fizz"
    if i % 5 == 0:
        num += "Buzz"
    print(num or i)
