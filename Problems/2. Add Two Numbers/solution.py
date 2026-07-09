class Solution(object):
    def modify(self, x):
        if type(x) == list:
            s = ""
            for i in x:
                s += str(i)
            s = "".join(reversed(s))
            return int(s)

        if type(x) == int:
            x = str(x)
            array = []
            for i in x:
                array.append(int(i))
            array.reverse()
            return array

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1 = self.modify(l1)
        l2 = self.modify(l2)
        # result = l1 + l2
        result = self.modify(l1 + l2)
        return result


sol = Solution()
l1 = [1, 2, 6]
l2 = [5, 6, 7]

result = sol.addTwoNumbers(l1, l2)
print(result)
