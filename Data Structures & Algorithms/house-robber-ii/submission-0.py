class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.dp(nums[1:]), self.dp(nums[:-1]))

    
    def dp(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        cur_max = nums[0]

        for i in range(2, n):
            nums[i] += cur_max
            cur_max = max(cur_max, nums[i - 1])

        return max(nums[-1], nums[-2])




        