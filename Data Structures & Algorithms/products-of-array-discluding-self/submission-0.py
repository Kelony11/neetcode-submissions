class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix = result[i - 1] * nums[i - 1]
            result[i] = prefix

        post_fix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * post_fix
            post_fix *= nums[i]

        return result

