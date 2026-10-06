class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        check = set(nums)
        
        ans = 0
        for i, x in enumerate(nums):
            
            if x - 1 not in check:
                
                curr = x
                streak = 1

                while curr + 1 in check:
                    curr += 1
                    streak += 1

                ans = max(ans, streak)
                
        return ans




        