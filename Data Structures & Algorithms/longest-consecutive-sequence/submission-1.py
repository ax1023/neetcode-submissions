class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        lookup = set(nums)

        mx = 0

        for i in lookup:
            if i - 1 not in lookup:
                l = 1

                while i + l in lookup:
                    l += 1

                mx = max(l, mx)

        return mx