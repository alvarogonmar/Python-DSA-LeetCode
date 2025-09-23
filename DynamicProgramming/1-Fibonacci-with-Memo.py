memo = [None] * 100
counter = 0

def fib(n):
    global counter
    counter += 1

    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n
