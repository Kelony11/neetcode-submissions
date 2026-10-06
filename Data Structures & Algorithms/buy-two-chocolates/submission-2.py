class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        first = float("inf")
        second = float("inf")

        for i, x in enumerate(prices):

            if x < first:
                first, second = x, first
            elif first <= x < second:
                second = x

        print("f", first, "s", second)

        res = money - (first + second)

        return res if res >= 0 else money


