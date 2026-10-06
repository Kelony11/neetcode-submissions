class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:


        for i in range(len(nums)):

            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:

                idx = nums[i] - 1

                nums[i], nums[idx] = nums[idx], nums[i]

        print("nums", nums)
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return nums[-1] + 1



            



        