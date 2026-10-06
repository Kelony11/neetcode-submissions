class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(sub, start_i):

            result.append(sub[:])

            for i in range(start_i, len(nums)):
                sub.append(nums[i])
                backtrack(sub, i + 1)
                sub.pop()

        backtrack([], 0)
        return result