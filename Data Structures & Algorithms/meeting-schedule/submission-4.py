"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if intervals == []:
            return True

        intervals.sort(key=lambda pair: pair.start)
        # intervals.sort(key=lambda pair: pair[0])

        curr_meetings = [(intervals[0].start, intervals[0].end)]

        for i in range(1, len(intervals)):
            
            start, end = intervals[i].start, intervals[i].end

            if start < curr_meetings[-1][1] and end < curr_meetings[-1][1]:
                print(curr_meetings) 
                return False
            elif start >= curr_meetings[-1][1] and end >= curr_meetings[-1][1]:
                curr_meetings.append((start, end))
            else:
                return False

            
        return True if len(curr_meetings) == len(intervals) else False


