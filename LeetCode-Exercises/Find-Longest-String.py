# WRITE FIND_LONGEST_STRING FUNCTION HERE #
#                                         #
#                                         #
#                                         #
#                                         #
###########################################
def find_longest_string(string_list):

    if not string_list:   # lista vacía
        return ""
        
    max_string = 0
    for word in string_list:
        max_string = max(max_string, len(word))
        
    for word in string_list:
        if max_string == len(word):

        


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""