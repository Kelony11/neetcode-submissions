class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        _map = Counter(hand)
        # print("init first _map", _map)

        while len(_map) >= 1:
            _min = min(_map.keys())

            print("first _min", _min)

            for _ in range(groupSize):
                if _min not in _map:
                    return False 
                
                _map[_min] -= 1
                if _map[_min] == 0: del _map[_min]
                _min += 1
                
        return True
            

        # print("_map", _map)

        


        