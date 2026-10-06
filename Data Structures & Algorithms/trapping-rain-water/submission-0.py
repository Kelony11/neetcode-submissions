class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        l, r = 0, n - 1

        MaxL, MaxR = height[l], height[r]

        # summing up the diff betweent the max and curr element 
        # both from the left and right pointers
        ans = 0

        while l <= r:
            # print("(l, r)", (l, r))

            MaxL = max(MaxL, height[l])
            # print("MaxL", MaxL)

            MaxR = max(MaxR, height[r])
            # print("MaxR", MaxR)

            if height[l] < height[r]:

                diff_l = MaxL - height[l]
                # print("diff_l", diff_l)

                ans += (diff_l)
                # print("ans++", ans)

                l += 1
                # print("l++", l)
            else:
                diff_r = MaxR - height[r]
                # print("diff_r", diff_r)

                ans += (diff_r)
                # print("ans++", ans)

                r -= 1
                # print('r--', r)

        return ans




        