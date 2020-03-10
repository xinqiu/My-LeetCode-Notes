class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        neg = 1
        if str == '':
            return 0
        if str and (str[0]=='+' or str[0] == '-'):
            if str[0] == '-':
                neg = -1
            str = str[1:]
        ret = ''
        for c in str:
            if c.isdigit():
                ret += c
            else:
                break
        if not ret:
            return 0
        return max(min(int(ret) * neg, 2**31-1), -2**31)

solution = Solution()

print(solution.myAtoi('   -42'))
