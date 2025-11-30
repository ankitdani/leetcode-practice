'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

'''
intervals = [1,3],[2,4],[5,6]
result = [1,4],[5,6]

prev = [1,3]
curr = [2,4]
if prev[1] >= curr[0] = true
new_start = min(prev[0], curr[0])
new_end = max(prev[1], curr[1])
prev = [new_start, new_end]
result = [1,4]

prev = [1,4]
curr = [5,6]
if prev[1] >= curr[0] = false
prev = curr
then continue to next iteration
result = [1,4]

since there are no more intervals exit loop

after loop exit, add prev to result

result = [1,4],[5,6]

Time: O(nlogn)
Space: O(n)
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda interval: interval[0])
        prev = intervals[0]
        result = []
        for i in range(1, n):
            curr = intervals[i]
            if prev[1] >= curr[0]:
                new_start = min(prev[0], curr[0])
                new_end = max(prev[1], curr[1])
                prev = [new_start, new_end]
            else:
                result.append(prev)
                prev = curr
        result.append(prev)
        return result
            
