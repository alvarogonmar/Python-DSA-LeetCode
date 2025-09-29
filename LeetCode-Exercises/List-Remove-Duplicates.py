# WRITE REMOVE_DUPLICATES FUNCTION HERE #
#                                       #
#                                       #
#                                       #
#                                       #
#########################################
    
def remove_duplicates(nums):
    if not nums:
        return 0
    l = 0
    r = 1
    
    while r < len(nums):
        if nums[l] == nums[r]:
            r += 1


