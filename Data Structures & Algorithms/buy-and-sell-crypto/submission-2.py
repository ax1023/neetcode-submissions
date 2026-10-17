class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        res = 0

        length = len(prices) - 1

        while (r <= length):
            cur_profit = prices[r] - prices[l]

            if cur_profit > res:
                res = cur_profit

            if prices[r] < prices[l]:
                l = r
            else:
                r += 1

        return res


        