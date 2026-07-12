case1 = ([3, 2, 3],)
case2 = ([2, 2, 1, 1, 1, 2, 2],)


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        n = len(nums) // 2

        for num, freq in count.items():
            if freq > n:
                return num, count
            
s = Solution()
print(s.majorityElement(*case1))
print(s.majorityElement(*case2))