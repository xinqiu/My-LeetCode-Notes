class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []

        for c in set(nums1) & set(nums2):
            ret.extend([c] * min(nums1.count(c), nums2.count(c)))
        return ret

# return [c for c in set(nums1) & set(nums2) for _ in range(min(nums1.count(c), nums2.count(c)))]


solution = Solution()

print solution.intersect([1,2,2,1], [2,2])