class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 0, 0

        n = len(nums)

        while r < n:
            # print("(l, r)", (l, r))

            count = 1 # count of the unique element

            while r + 1 < n and nums[r] == nums[r + 1]:
                count += 1
                # print("count++", count)
                r += 1
                # print("r++", r)

            # replace k elements
            for k in range(min(count, 2)):
                # print("k", k)
                nums[l] = nums[r]
                l += 1
                # print("l++", l)

            r += 1
            # print("iterator", "r++", r)

        return l

            



