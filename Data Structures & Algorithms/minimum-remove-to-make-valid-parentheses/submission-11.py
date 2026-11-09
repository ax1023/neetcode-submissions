class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == "":
            return s


        indices = []

        pair = {"}": "{", 
        ")": "(",
        "]": "["}

        open_p = {"(", "[", "{"}

        for i in range(len(s)):
            if s[i] in open_p:
                indices.append(i)
            elif s[i] in pair:
                if indices and pair[s[i]] == s[indices[-1]]:
                    indices.pop()
                else:

                    indices.append(i)

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
            


            

                

        
        