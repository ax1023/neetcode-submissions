class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]

        ref = {"]": "[",
               "}": "{",
               ")": "("}
        
        for i in range(1, len(s)):
            if s[i] in ref and stack and ref[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
            print(stack)

        return len(stack) == 0