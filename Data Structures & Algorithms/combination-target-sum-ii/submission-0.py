class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        candidates.sort()

        def backtrack(curr, sub, start_i):

            if curr == target:
                result.append(sub[:])
                return

            if curr > target or start_i >= len(candidates):
                return
  
            for i in range(start_i, len(candidates)):
                
                if i > start_i and candidates[i] == candidates[i - 1]:
                    continue

                sub.append(candidates[i])
                backtrack(curr + candidates[i], sub, i + 1)
                sub.pop()

        backtrack(0, [], 0)
        return result

        