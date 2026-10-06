class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.result = []

        def backtrack(i, path, path_sum):
            # print("i", i, "path", path)

            if path_sum > target or i >= len(nums):
                # print("stop")
                return 
            
            if path_sum == target:
                # print("path_sum", path_sum)
                self.result.append(path[:])
                # print("got it!", self.result)
                return 

            for j in range(i, len(nums)):
                path.append(nums[j])
                path_sum += nums[j]
                backtrack(j, path, path_sum)
                path.pop()
                path_sum -= nums[j]
            

        backtrack(0, [], 0)

        return self.result