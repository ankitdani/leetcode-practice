'''
Docstring for 435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
'''

'''
intervals = [1,3],[4,6],[5,7]
result = 1

to find min number of intervals to remove so that no intervals are overlapping
logic = 

greedy approach = keep the intervals that end 1st
sort by end time 
by sorting on end time, we have max space for other intervals to keep
if any interval overlaps, then count them and subtract by total intervals


Time: O(nlogn)
Space: O(1)
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x:x[1])
        keep = 1
        prev_end = intervals[0][1]
        for i in range(1, n):
            curr_start, curr_end = intervals[i]
            if curr_start >= prev_end:
                keep += 1
                prev_end = curr_end
        return n - keep