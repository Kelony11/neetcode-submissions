"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start_arr = sorted([i.start for i in intervals])
        end_arr = sorted([i.end for i in intervals])

        num_days, result = 0, 0

        s , e = 0, 0

        while s < len(start_arr):
            if start_arr[s] < end_arr[e]:
                s += 1
                num_days += 1
            else: # If it's both tie or start_arr[s] > end_arr[e]
                e += 1
                num_days -= 1
            result = max(result, num_days)
        
        return result
            
