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
            l += 1
        elif prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxi = max(maxi, profit)
            r += 1
    return maxi
    


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
