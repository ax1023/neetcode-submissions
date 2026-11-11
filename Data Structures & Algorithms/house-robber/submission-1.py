class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = nums.copy()

        n = len(nums)

        if n == 1:
            return dp[0]
        elif n == 2:
            return max(dp[0], dp[1])

        cur_max = dp[0]

        for i in range(2, n):
            dp[i] += cur_max
            cur_max = max(cur_max, dp[i - 1])

        return max(dp[-1], dp[-2])



    # 1, 2, 3, 1  


    # 1, 2, 4,     