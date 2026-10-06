class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(sub, start_i):

            if sum(sub) > target or start_i >= len(nums):
                return

            if sum(sub) == target:
                result.append(sub[:])
                return 

            for i in range(start_i, len(nums)):
                sub.append(nums[i])
                backtrack(sub, i)
                sub.pop()


        backtrack([], 0)
        return result

        