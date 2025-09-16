## WRITE SELECTION_SORT FUNCTION HERE ##
#                                      #
#                                      #
#                                      #
#                                      #
########################################

def selection_sort(my_list): # selection sort function
    for i in range(len(my_list) - 1): # for i in range from 0 to the second last element
        min_index = i # assume the minimum is the first element
        for j in range(i+1, len(my_list)): # for j in range from i+1 to the end of the list
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list




print(selection_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

