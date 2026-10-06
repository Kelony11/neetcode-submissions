class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        result = []

        right_max = float("-inf")

        for i in range(len(heights) - 1, -1, -1):

            if heights[i] > right_max:
                result.append(i)

            right_max = max(right_max, heights[i])

        return result[::-1]

            



        