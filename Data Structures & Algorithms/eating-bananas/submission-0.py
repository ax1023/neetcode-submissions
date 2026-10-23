class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        res = max(piles)
        l = 1
        r = res

        while l <= r:
            mid = l + (r - l) // 2 

            h_cur = 0

            for i in piles:
                h_cur += math.ceil(float(i) / mid)

            if h_cur <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res

            


        