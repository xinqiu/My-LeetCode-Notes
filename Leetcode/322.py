class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [1e9] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != 1e9 else -1


solution = Solution()

print solution.coinChange([186,419,83,408], 6249)
