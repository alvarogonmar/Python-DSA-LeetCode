def funcThree(): # Function that calls itself
    print('Three') # Base case is not needed here, but it could be added for a real recursive function

def funcTwo(): # Function that calls another function
    funcThree()
    print('Two')

def funcOne():
    funcTwo()
    print('One')


funcOne()

