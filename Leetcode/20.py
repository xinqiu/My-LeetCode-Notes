class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        m = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack:
                    if m[c] != stack[-1]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

solution = Solution()
print(solution.isValid('(]'))

'''
class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
'''