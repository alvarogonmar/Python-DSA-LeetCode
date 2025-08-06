def factorial(n): # Function to calculate factorial of n
    if n == 1: # Base case for recursion
        return 1
    return n * factorial(n-1)


print(factorial(4))

