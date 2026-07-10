case1 = ([1, 1, 1, 2, 2, 3],)
case2 = ([0, 0, 1, 1, 1, 1, 2, 3, 3],)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return len(nums)

        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
    
s = Solution()
print(s.removeDuplicates(*case1))
print(s.removeDuplicates(*case2))