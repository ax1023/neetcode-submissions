class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}

        for i in range(len(nums)):
            if nums[i] in ref:
                j = ref[nums[i]]
                return [i, j] if i < j else [j, i]

            ref[target - nums[i]] = i


        