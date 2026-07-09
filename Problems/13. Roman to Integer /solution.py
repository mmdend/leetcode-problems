s1 = "LVIII"
s2 = "III"
s3 = "MCMXCIV"

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }
        s = list(s)
        result = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        result += roman[s[-1]]
        return result

cl = Solution()
print(cl.romanToInt(s1))
print(cl.romanToInt(s2))
print(cl.romanToInt(s3))

