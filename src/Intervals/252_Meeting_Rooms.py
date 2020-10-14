#[[0,30],[5,10],[15,20]]
#--------------------------------
#[0                           30]
#      [5   10]
#                   [15  20]
def canAttendMeetings(intervals):
    if not intervals:
        return True
    intervals.sort()
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        cur_start = intervals[i][0]
        cur_end = intervals[i][1]
        if cur_end < end:
            return False
       end = cur_end
    return True

# Time complexity: O(nlogn)
# Space Complexity: O(1)
