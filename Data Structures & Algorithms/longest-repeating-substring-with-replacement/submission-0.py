class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occurrences = {}
        l = 0
        r = 0

        res = 0

        most_freq_app = 0

        while r < len(s):
            occurrences[s[r]] = occurrences.get(s[r], 0) + 1
            most_freq_app = max(most_freq_app, occurrences[s[r]])

            while (r - l + 1) - most_freq_app > k:
                occurrences[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)
            r += 1

        return res


        