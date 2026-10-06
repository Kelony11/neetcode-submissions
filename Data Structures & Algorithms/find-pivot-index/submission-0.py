class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        post = sum(nums)
        pre = 0

        for i, x in enumerate(nums):
            # print("i", i, "x", x)

            post -= x
            # print("post", post)

            if pre == post:
                return i

            pre += x
            # print("pre", pre)

        return -1




        