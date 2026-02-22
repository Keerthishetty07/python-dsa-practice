# Problem: Best Time to Buy and Sell Stock (LeetCode #121)
# Approach: Greedy + Prefix Minimum Tracking (Single Pass)
# Time: O(n)
# Space: O(1)
# Insight: Track minimum price so far and compute profit if selling today

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


# Example run
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
