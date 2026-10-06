class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        if k == 1:
            return 0

        splits = []
        for i in range(1, len(weights)):

            splits.append(weights[i - 1] + weights[i])

        splits.sort()
        # print("splits", splits)
        
        k = k - 1 # index starts from 0

        max_score = sum(splits[-k:])
        min_score = sum(splits[:k])

        # print("min", min_score, "max", max_score)
        return max_score - min_score