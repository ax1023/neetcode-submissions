class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        res = 0

        length = len(prices) - 1

        while (l <= length - 1) and (r <= length):
            if prices[r] - prices[l] > res:
                res = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l, r = r, r + 1
            else:
                r += 1

        return res


        