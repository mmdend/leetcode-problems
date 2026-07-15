case1 = ([7, 1, 5, 3, 6, 4],)
case2 = ([1, 2, 3, 4, 5],)
case3 = ([7, 6, 4, 3, 1],)


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


s = Solution()
print(s.maxProfit(*case1))
print(s.maxProfit(*case2))
print(s.maxProfit(*case3))
