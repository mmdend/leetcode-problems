case1 = ([3,2,2,3], 3)
case2 = ([0,1,2,2,3,0,4,2], 2)


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        del nums[k:]
        return k, nums
    

s = Solution()
print(s.removeElement(*case1))
print(s.removeElement(*case2))