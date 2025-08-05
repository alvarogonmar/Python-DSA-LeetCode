def funcThree(): # Function that calls itself
    print('Three')

def funcTwo():
    funcThree()
    print('Two')

def funcOne():
    funcTwo()
    print('One')


funcOne()

