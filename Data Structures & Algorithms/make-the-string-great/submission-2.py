class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = [s[0]]

        for i in range(1, len(s)):
            if stack and (ord(stack[-1]) == (ord(s[i]) - 32) or ord(stack[-1]) == (ord(s[i]) + 32)):
                stack.pop()
            else:
                stack.append(s[i])


        return "".join(stack)
             
