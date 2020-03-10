class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)

solution = Solution()

print solution.reverseBits(00000010100101000001111010011100)