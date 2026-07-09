c1 = ["flower", "flow", "flight"]
c2 = ["dog", "racecar", "car"]


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        min_str = strs[0]
        for string in strs:
            if len(string) < len(min_str):
                min_str = string

        prefix = ""

        for i in range(len(min_str)):
            current_char = strs[0][i]

            for string in strs:
                if string[i] != current_char:
                    return prefix

            prefix += current_char

        return prefix
    

exe = Solution()
print(exe.longestCommonPrefix(c1))
print(exe.longestCommonPrefix(c2))
