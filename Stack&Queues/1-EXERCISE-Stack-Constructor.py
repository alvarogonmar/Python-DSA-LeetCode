# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
        
# class Stack:
    ## WRITE STACK CONSTRUCTOR HERE ##
    #                                #
    #                                #
    #                                #
    #                                #
    ##################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node


my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""