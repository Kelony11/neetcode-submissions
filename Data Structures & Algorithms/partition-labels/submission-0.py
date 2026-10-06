from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        _map = defaultdict(int)

        for i, x in enumerate(s):
            # print("i", i, "x", x)
            _map[x] = i

        # print("_map", _map)

        start, end = 0, 0

        result = []

        for i, x in enumerate(s):
            # print("i", i, "x", x)
            end = max(end, _map[x])
            # print("end", end)

            if i == end:
                result.append(end - start + 1)
                # print("result", result)
                start = i + 1
        return result
            
        
