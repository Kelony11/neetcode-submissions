class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        five, ten, twenty = 0, 0, 0

        for i, b in enumerate(bills):
            # print("i", i, "x", b)

            if b == 5:
                five += 1
            elif b == 10:
                if five <= 0:
                    return False
                five -= 1
                ten += 1
            elif b == 20:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False
            
            # print("5", five, "10", ten, "20", twenty)
        return True
            

                
                    
        