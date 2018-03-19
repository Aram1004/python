def fibonacci(n):
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in list:
        print(n)

    f(n) = 0 if n = 0
    f(n) = 1 if n = 1
    f(n) = f(n-1) + f(n-2) if n > 1

    for i in range(11):
        print("f(%d) = %d" % (i, fibonacci(i)))
