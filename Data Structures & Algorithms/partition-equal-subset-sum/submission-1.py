class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 == 1:
            return False 

        target = total // 2

        dp = [False] * (target + 1) 
        dp[0] = True

        for n in nums:
            # t == target .... n
            for t in range(target, n - 1, -1):
                # For each number, update the DP from right to left 
                # so that each number is used only once.
                # This avoids overwriting results from the same iteration.

                dp[t] = dp[t] or dp[t - n]

            print("dp", dp)

        return dp[target]

        