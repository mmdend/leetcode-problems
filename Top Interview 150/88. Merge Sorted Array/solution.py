case1 = ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
case2 = ([1], 1, [], 0)
case3 = ([0], 0, [1], 1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]

        l = m + n
        for i in range(l):
            swapped = False
            for j in range(0, l - i - 1):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
                    swapped = True
            if not swapped:
                break
        return nums1

s = Solution()
print(s.merge(*case1))
print(s.merge(*case2))
print(s.merge(*case3))