class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words = {}
        res = []

        mx = 0

        for i in range(len(strs)):
            srtd = "".join(sorted(strs[i]))
            if srtd in words:
                res[words[srtd]].append(strs[i])
            else :
                words[srtd] = mx
                res.append([strs[i]])
                mx += 1

        return res
            


        