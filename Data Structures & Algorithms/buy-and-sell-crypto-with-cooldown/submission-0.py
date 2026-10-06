class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prev_buy = -prices[0]
        prev_sell, prev_cool = 0, 0

        for i in range(len(prices)):
            # print("i", i)

            curr_buy = max(prev_buy, prev_cool - prices[i])
            # print("x", curr_buy)
            curr_sell = prices[i] + prev_buy
            # print("y", curr_sell)

            curr_cool = max(prev_sell, prev_cool)
            # print("z", curr_cool)

            prev_buy = curr_buy
            # print("a", prev_buy)
            prev_sell = curr_sell
            # print("b", prev_sell)
            prev_cool = curr_cool
            # print("c", prev_cool)

        return max(prev_sell, prev_cool)
        