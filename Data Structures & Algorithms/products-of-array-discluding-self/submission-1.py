class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix = [1] * n

        for i in range(1, n):

            prefix[i] = prefix[i - 1] * nums[i - 1]

        # print("prefix", prefix)

        post = 1

        for i in range(n - 1, -1, -1):
            prefix[i] *= post
            # print("prefix", prefix)

            post *= nums[i]
            # print("post", post)
        
        return prefix



        