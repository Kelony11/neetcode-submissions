class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        total = 0

        size = float("inf")

        for r in range(len(nums)):
            print("r", r)

            total += nums[r]
            # print("total++", total)

            while total >= target:

                size = min(size, r - l + 1)
                # print("size", size)

                total -= nums[l]
                # print("total--", total)

                l += 1
                # print("r", r, "l++", l)

        return size if size != float('inf') else 0
        