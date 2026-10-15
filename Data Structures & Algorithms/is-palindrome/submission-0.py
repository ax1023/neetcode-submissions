class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        def is_alpha(c):
            if (48 <= ord(c) <= 57 or 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122):
                return True
            return False
            

        while l <= r:
            if not is_alpha(s[l]):
                l += 1
                continue
            if not is_alpha(s[r]):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

        