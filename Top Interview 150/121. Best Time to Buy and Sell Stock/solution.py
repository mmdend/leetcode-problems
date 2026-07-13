case1 = ([7,1,5,3,6,4],)
case2 = ([7,6,4,3,1],)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy = prices[0]
        # profit = sell - buy
        max_profit = 0

        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > max_profit:
                max_profit = price - buy

        return max_profit

s = Solution()
print(s.maxProfit(*case1))  # Output: 5
print(s.maxProfit(*case2))  # Output: 0