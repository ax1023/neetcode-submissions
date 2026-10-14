class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        mul_up_to_i = 1

        for i in nums:
            res.append(mul_up_to_i)
            mul_up_to_i *= i

        
        mul_rev = 1
        for i in range(len(nums), 1, -1):
            mul_rev = mul_rev * nums[i - 1]
            res[i - 2] *= mul_rev


        return res

            
        