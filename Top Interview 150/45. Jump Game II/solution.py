case1 = ([2, 3, 1, 1, 4],)
case2 = ([2, 3, 0, 1, 4],)
case3 = ([5, 3, 0, 1, 4],)


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        currentEnd = 0
        far = 0

        for i in range(len(nums) - 1):
            if i + nums[i] > far:
                far = i + nums[i]

            if i == currentEnd:
                jumps += 1
                currentEnd = far

        return jumps


s = Solution()
print(s.jump(*case1))
print(s.jump(*case2))
print(s.jump(*case3))
