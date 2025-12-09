'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
'''

'''
intervals = [1,3],[4,6]
insert = [2,5]

result = [1,6]

add all previous intervals whose intervals[1] < new_interval[0]
update new_interval if interval[0] <= new_interval[1]
add all rest 

Time: O(n)
Space: O(n)
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        result = []
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            new_start = min(intervals[i][0], newInterval[0])
            new_end = max(intervals[i][1], newInterval[1])
            newInterval = [new_start, new_end]
            i += 1
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        return result