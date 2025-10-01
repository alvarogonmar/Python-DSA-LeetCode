# WRITE MAX_PROFIT FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################
def max_profit(prices):
    maxi = 0
    
    l, r = 0, 1
    
    while r < len(prices):
        if prices[r] < prices[l]:
            r += 1
