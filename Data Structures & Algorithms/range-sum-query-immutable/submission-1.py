class NumArray:

    def __init__(self, nums: List[int]):

        self.prefix = [nums[0]]

        for i in range(1, len(nums)):
            # print("x", nums[i])

            self.prefix.append(self.prefix[-1] + nums[i])
            # print("self.prefix", self.prefix)

        return None

    def sumRange(self, left: int, right: int) -> int:
        
        self.left = self.prefix[left - 1] if left > 0 else 0
        self.right = self.prefix[right]

        return (self.right - self.left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)