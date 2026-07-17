case1 = ([3, 0, 6, 1, 5],)
case2 = ([1, 3, 1],)


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        # citations = [0, 1, 3, 5, 6]

        n = len(citations)
        for i in range(n):
            h = n - i

            if citations[i] >= h:
                return h


        return 0
    
s = Solution()
print(s.hIndex(*case1))
print(s.hIndex(*case2))