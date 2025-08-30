## WRITE BUBBLE_SORT FUNCTION HERE ##
#                                   #
#                                   #
#                                   #
#                                   #
##################################### 
    

def bubble_sort(my_list): # def inicializadora de bubblesort
    for i in range(len(my_list) - 1, 0, -1): # for i in range from the end of the list to the beginning
        for j in range(i): # for j in range from 0 to i
            if my_list[j] > my_list[j+1]: # if the current element is greater than the next element
                temp = my_list[j] # swap the elements
                my_list[j] = my_list[j+1] # move the next element to the current position
                my_list[j+1] = temp # move the current element to the next position
    return my_list



print(bubble_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """