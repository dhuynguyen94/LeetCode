class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals)
        room = []
        heapq.heappush(room, intervals[0][1]) # Add ending time of 1st room
        for i in intervals[1:]: # Look other rooms
            if room[0] <= i[0]:  # start time of new room > ending time 
                heapq.heappop(room)
            heapq.heappush(room, i[1])
        return len(room)
