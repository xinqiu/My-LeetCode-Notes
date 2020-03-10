class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        isPrime = [True for _ in range(n)]

        for i in range(2, int(n ** 0.5)+1):
            if isPrime[i]:
                # for j in range(i ** 2, n, i):
                #     isPrime[j] = False
                isPrime[i*i:n:i] = [False] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime[2:])

solution = Solution()


print solution.countPrimes(10)