class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        # It takes the 0 - target[0] steps to start
        ans = target[0]

        n = len(target)

        for i in range(1, n):
            # print("i", i)

            if target[i] > target[i - 1]:
                ans += (target[i] - target[i - 1])
            
        return ans


        