class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1

        if s == "":
            return 0

        res = 1

        l = 0
        r = 0

        seen = {}

        while r < len(s):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
            

        return res
