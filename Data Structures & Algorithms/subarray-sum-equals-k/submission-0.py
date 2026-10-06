from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        prefix = 0

        count = 0

        for i, x in enumerate(nums):
            # print("i", i, "x", x)

            prefix += x
            # print("prefix++", prefix)

            diff = prefix - k
            # print("diff", diff)

            count += prefix_map[diff]
            # print("count++", count)

            prefix_map[prefix] += 1
            # print("prefix_map", prefix_map)

        return count
                    

