class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        seen = {}
        for i in s:
            seen[i] = seen.get(i, 0) + 1

        for j in t:
            if j not in seen:
                return False

            if seen[j] == 0:
                return False

            seen[j] -= 1

        return True
    

    
        