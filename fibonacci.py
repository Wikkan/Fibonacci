def fib(n):
    a = 0
    b = 1
    i = 0
     
    for x in range(n):
        a, b = b, a+b
    return a