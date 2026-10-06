class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 1, 1

        while r < len(nums):

            if nums[r - 1] != nums[r]:
                
                nums[l] = nums[r]
                l += 1
                # print("l++", l)
            
            r += 1
            # print("r++", r)

            # print("nums", nums)

        return l
            
             


        