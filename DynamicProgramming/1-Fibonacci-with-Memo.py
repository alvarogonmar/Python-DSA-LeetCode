memo = [None] * 100 # Assuming n will not exceed 99
counter = 0 # To count the number of function calls

def fib(n): # Using memoization
    global counter
    counter += 1

    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

n = 7
print("Fib of" , n, "=", fib(n))
print("Counter: ", counter)