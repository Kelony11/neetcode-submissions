class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        max_amount = amount + 1
        dp = [max_amount for _ in range(max_amount)]
        dp[0] = 0

        # print("dp", dp)

        for i in range(1, len(dp)):

            for c in coins:
                
                subtract = i - c

                if subtract >= 0 :
                    dp[i] = min(dp[i], dp[subtract] + 1)

        # print("dp", dp)
        return dp[-1] if dp[-1] != max_amount else -1
        