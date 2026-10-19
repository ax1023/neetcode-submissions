class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(temperatures)


        for i in range(1, len(temperatures)):
            while temperatures[i] > temperatures[stack[-1]]:
                cur = stack.pop()
                res[cur] = i - cur
                if not stack:
                    break
                    
            stack.append(i)      

        return res
                

                # [30,38,30,36,35,40,28]

                # stack = 38,  

                #res[1, 0, 1, 2, 1, 0, 0]


        