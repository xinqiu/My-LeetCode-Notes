class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = sum([secret[i] == guess[i] for i in range(len(secret))])
        from collections import Counter
        B = sum((Counter(secret) & Counter(guess)).values()) - A

        return "%dA%dB" %(A, B)

solution = Solution()

print solution.getHint("11223", "01112")
