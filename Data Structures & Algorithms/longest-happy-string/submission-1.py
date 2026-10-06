class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        # sort O(1) = 3 element 
        # check for last two, then move to the next max

        _map = {"a": a, "b": b, "c": c}

        result = ""

        while True:
            
            output = sorted(_map.items(), key=lambda x: x[1], reverse=True)
            # print("output", output)

            first_c, first_freq = output[0]
            second_c, second_freq = output[1]

            # print("max_c", first_c, "max_freq", first_freq)

            placed = False
            for i in range(_map[first_c]):
                if len(result) >= 2 and result[-1] == first_c and result[-2] == first_c:
                    # go the second max 
                    if _map[second_c] > 0:
                        result += second_c
                        _map[second_c] -= 1
                        # print("Update", _map)
                        # print("result", result)
                        placed = True
                    continue

                if _map[first_c] > 0:
                    # stick with the first max 
                    result += first_c
                    _map[first_c] -= 1
                    # print("Update", _map)
                    # print("result", result)
                    placed = True 

            
            if not placed:
                break

        return result



            
        