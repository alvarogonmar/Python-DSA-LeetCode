def factorial(n): # Function to calculate factorial of n
    if n == 1: # Base case for recursion
        return 1 # If n is 1, return 1
    return n * factorial(n-1) # Recursive call to calculate factorial of n-1


print(factorial(4)) # This will print the factorial of 4, which is 24

