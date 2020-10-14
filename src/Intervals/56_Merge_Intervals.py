# [[1,4],[4,5]]
# ------------------
# 1           4 
#             4    5 

# [[1,3],[2,6],[8,10],[15,18]]
# -----------------------------
# 1----3
#    2-------6
#                8--10
#                        15---18     


def mergeInterval(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]
        if start <= merged[-1][-1]:
            merged[-1][-1] = max(merged[-1][-1], end)
        else:
            merged.append(intervals[i])
    return merged

    #Time complexity: O(nlogn)
    #Space complexity: O(n) if uses extra merged array.