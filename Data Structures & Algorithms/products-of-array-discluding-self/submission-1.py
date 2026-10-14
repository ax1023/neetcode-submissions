class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        mul_counter = 1

        for i in nums:
            res.append(mul_counter)
            mul_counter *= i

        
        mul_counter = 1
        for i in range(len(nums), 1, -1):
            mul_counter = mul_counter * nums[i - 1]
            res[i - 2] *= mul_counter


        return res

            
        