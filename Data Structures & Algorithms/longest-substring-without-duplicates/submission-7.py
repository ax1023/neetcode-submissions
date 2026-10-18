class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1

        if s == "":
            return 0

        res = 1

        l = 0
        r = 1

        seen = set()
        seen.add(s[l])
        # s="pwwkew"

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen and l <= r:
                    seen.discard(s[l])
                    l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
            r += 1
            

        return res
