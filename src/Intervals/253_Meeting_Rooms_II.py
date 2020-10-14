#[[0, 30],[5, 10],[15, 20]]
# ------------------------------
# 0---------------------------30        room 1
#       5----10                         room 2
#                 15----20              room 2

import heapq
def meetingRoomII(intervals):
    if not intervals:
        return 0
    heap = [intervals[0][1]]
    intervals.sort()

    for i in range(1, len(intervals)):
        cur_start = intervals[i][0]
        cur_end = intervals[i][1]
        next_available = heapq.heappop(heap)
        if cur_start < next_available:
            heapq.heappush(heap, next_available)
        heapq.heappush(heap, cur_end)
    return len(heap)

intervals = [[0,30],[5,10],[15,20]]

print(meetingRoomII(intervals))


# Time Complexity: O(nlogn)
# Space complexity: O(n)