for num in range(0,11):
    fact = 1
    if num == 0:
        print("factorial of zero is 1")
    else:
        for i in range(1, num + 1):
            fact = fact * i
        print("The factorial of", num, "is:", fact)
