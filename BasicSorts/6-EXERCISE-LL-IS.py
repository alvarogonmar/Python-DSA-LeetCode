class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList: # Singly Linked List
    def __init__(self, value): # Initialize with head and tail pointers
        new_node = Node(value) # Create the first node
        self.head = new_node # Head points to the first node
        self.tail = new_node # Tail also points to the first node
        self.length = 1 # Initialize length

    def print_list(self): # Print all values in the list
        temp = self.head # Start from the head
        while temp is not None: # Traverse until the end
            print(temp.value) # Print the current node's value
            temp = temp.next # Move to the next node
        
    def append(self, value): # Append a new node to the end of the list
        new_node = Node(value) # Create a new node
        if self.head is None: # If the list is empty
            self.head = new_node # Head points to the new node
            self.tail = new_node # Tail also points to the new node
        else:
            self.tail.next = new_node # Link the current tail to the new node
            self.tail = new_node # Update the tail to the new node
        self.length += 1 # Increment the length

    # WRITE INSERTION_SORT METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################

    def insertion_sort(self): # Insertion Sort for Linked List
        if self.length < 2: # If the list has 0 or 1 node, it's already sorted
            return # No need to sort
        
        sorted_list_head = self.head # Start with the first node as the sorted part
        unsorted_list_head = self.head.next
        sorted_list_head.next = None # Detach the sorted part
        
        while unsorted_list_head is not None: # While there are nodes in the unsorted part
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next
            
            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
        
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

