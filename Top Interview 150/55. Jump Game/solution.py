case1 = ([2, 3, 1, 1, 4],)
case2 = ([3, 2, 1, 0, 4],)


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        steps = 0

        for i in range(0, len(nums)):
            if steps < 0:
                return  False
            elif nums[i] > steps:
                steps = nums[i]
            steps -= 1

        return True



s = Solution()
print(s.canJump(*case1))
print(s.canJump(*case2))

