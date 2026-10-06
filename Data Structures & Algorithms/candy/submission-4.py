class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)

        # initializing answer to be the length of the ratings 
        # Because every children get at least one candy

        result = [1] * n

        # Checking left neighbors
        
        for l in range(1, n):
            if ratings[l] > ratings[l - 1]:
                result[l] = max(result[l], result[l - 1] + 1)
        
        print("left result", result)
            
        for r in range(n - 2, -1, -1):
            if ratings[r] > ratings[r + 1]:
                result[r] = max(result[r], result[r + 1] + 1)

        # print("right result", result)

        return sum(result)


        


        