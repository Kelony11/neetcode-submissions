class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)

        l, r = 0, n - 1

        max_water = float("-inf")

        while l <= r:
            # print("(l, r)", (l, r))

            area = (r - l) * min(heights[l], heights[r])
            # print("area", area)

            if heights[l] < heights[r]:
                l += 1
                # print("l++", l)
            else:
                r -= 1
                # print('r--', r)

            max_water = max(max_water, area)
            # print("max_water", max_water)

        return max_water

        

            
            
        