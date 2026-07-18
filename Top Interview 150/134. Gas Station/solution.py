case1 = ([1,2,3,4,5], [3,4,5,1,2])
case2 = ([2,3,4], [3,4,3])

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                start = i + 1
                tank = 0

        if total < 0:
            return -1
        return start
    
s = Solution()
print(s.canCompleteCircuit(*case1))
print(s.canCompleteCircuit(*case2))