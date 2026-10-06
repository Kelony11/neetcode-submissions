class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        five, ten, twenty = 0, 0, 0

        for i, b in enumerate(bills):
            # print("i", i, "x", b)

            if b == 5:
                five += 1
            elif b == 10:
                five -= 1
                ten += 1
            elif b == 20:
                if five >= 3:
                    five -= 3
                    twenty += 1
                    continue 
                else:
                    five -= 1
                    ten -= 1
                    twenty += 1


            if five < 0 or ten < 0:
                return False
            
            # print("5", five, "10", ten, "20", twenty)
        return True
            

                
                    
        