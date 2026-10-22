class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        fleets = 1

        ps_and_sp = []

        for ps, sp in zip(position, speed):
            ps_and_sp.append((ps, sp))
        
        ps_and_sp.sort(reverse=True)

        for ps, sp in ps_and_sp:
            cur_arrival = (target - ps) / sp
            stack.append(cur_arrival)
            if len(stack) > 1 and cur_arrival <= stack[-2]:
                stack.pop()

        return len(stack)
            



        
        
        