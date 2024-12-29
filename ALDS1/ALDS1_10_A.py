FIB = [None]*50

def fib(n):
    if n <= 0: return 1
    if n == 1: return 1
    if FIB[n] is not None: return FIB[n]
    FIB[n] = fib(n-1) + fib(n-2)
    return FIB[n]

print(fib(int(input())))
