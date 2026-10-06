"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:












































































        

        # EDGE CASE 
        if intervals == []:
            return True

        intervals.sort(key=lambda pair: pair.start)
        # intervals.sort(key=lambda pair: pair[0])

        curr_meetings = [(intervals[0].start, intervals[0].end)]

        for i in range(1, len(intervals)):
            prev_end = curr_meetings[-1][1]
            
            start, end = intervals[i].start, intervals[i].end

            if ( 
                (start < prev_end and end < prev_end) 
                or (start, end) == curr_meetings[-1]
                ):
                return False
            elif start >= prev_end and end >= prev_end:
                curr_meetings.append((start, end))
        

        return True if len(curr_meetings) == len(intervals) else False


