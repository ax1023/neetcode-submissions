class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = 0
        r = 0

        occurrences = {}

        for i in range(len(s)):
            occurrences[s[i]] = i

        res = []
        l = 0
        r = 0

        mx = 0

        while r < len(s):
            mx = max(occurrences[s[r]], mx)
            if r == mx:
                res.append(r - l + 1)
                l = r + 1
            r += 1

        return res

            









        