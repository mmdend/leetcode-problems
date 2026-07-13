case1 = ([1,2,3,4,5,6,7], 3)
case2 = ([-1,-100,3,99], 2)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        k %= len(nums)
        p = len(nums) - k
        nums_last = nums[p:]
        nums_first = nums[:p]

        for i in range(1, k + 1):
            nums[-i] = 0
        
        for i in range(p):
            nums[k + i] = nums_first[i]

        for i in range(len(nums_last)):
            nums[i] = nums_last[i]

        return nums_last, nums_first, nums


# s = Solution()
# print(s.rotate(*case1))
# print(s.rotate(*case2))

# https://leetcode.com/problems/rotate-array/solutions/7184902/brute-force-to-optimised-approach-java-p-z4yy 


class Solution2:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)
        return nums

s = Solution2()
print(s.rotate(*case1))
print(s.rotate(*case2))