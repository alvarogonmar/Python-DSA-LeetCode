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
        else:
            l += 1
            nums[l] = nums[r]
            r += 1
    return l + 1

# Test case 1: Empty list
test1 = []
print(f"Test 1 Before: {test1}")
result1 = remove_duplicates(test1)


