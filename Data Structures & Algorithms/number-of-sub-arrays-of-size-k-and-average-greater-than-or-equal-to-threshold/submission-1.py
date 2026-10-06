class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        l = 0

        total_sum = 0

        ans = 0

        for r in range(len(arr)):
            # print("r", r)
            
            # Re-sizing the sub array
            while l < r and (r - l + 1) > k:
                # print("check l", l)
                # shrink from the left
                total_sum -= arr[l]
                # print("total_sum--", total_sum)

                l += 1
                # print("l++", l)

            total_sum += arr[r]
            # print("total_sum++", total_sum)

            # Check first
            if (r - l + 1) == k and (total_sum // k) >= threshold:
                ans += 1
                # print("ans++", ans)

        return ans
            



        