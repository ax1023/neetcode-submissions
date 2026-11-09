class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == "":
            return s

        stack = []
        indices = []

        pair = {"}": "{", 
        ")": "(",
        "]": "["}

        open_p = {"(", "[", "{"}

        for i in range(len(s)):
            if s[i] in open_p:
                stack.append(s[i])
                indices.append(i)
            elif s[i] in pair:
                if stack and pair[s[i]] == stack[-1]:
                    stack.pop()
                    indices.pop()
                else:
                    stack.append(s[i])
                    indices.append(i)

        print(stack, indices)
            

        if not indices:
            return s

        cur = 0

        res = ""

        for i in range(len(s)):
            if cur < len(indices) and i == indices[cur]:
                cur += 1
                continue
            else:
                res += s[i]

        return res
            


            

                

        
        