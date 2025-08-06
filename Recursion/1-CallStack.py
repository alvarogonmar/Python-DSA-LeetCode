def funcThree(): # Function that calls itself
    print('Three') # Base case is not needed here, but it could be added for a real recursive function

def funcTwo(): # Function that calls another function
    funcThree() # Call to funcThree, which will print 'Three'
    print('Two') # This will print 'Two' after 'Three'

def funcOne(): # Function that calls funcTwo
    funcTwo() # Call to funcTwo, which will print 'Two' and then 'Three'
    print('One')


funcOne()

