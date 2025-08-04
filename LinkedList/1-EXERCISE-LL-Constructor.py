# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################

# class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################
class Node:
    def __init__(self, value): # Funcion para crear un nodo
        self.value = value; # Valor del nodo
        self.next = None; # Siguiente nodo es None al inicio
        
class LinkedList: 
    def __init__(self, value): # Funcion para crear una lista enlazada
        new_node = Node(value); # Crear un nuevo nodo con el valor dado
        self.head = new_node;
        self.tail = new_node;
        self.length = 1;


 
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    