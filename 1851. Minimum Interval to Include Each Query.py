'''
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.
'''

'''
intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]
result= [3,3,1,4]

brute force = TLE - nested loops 

blocker = searching everytime

use heap to get sorted queries 
Time: O(nlogn + qlogq)
Space: O(n)
'''

# class Solution:
#     def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
#         result = []
#         for query in queries:
#             min_size = float('inf')
#             for l, r in intervals:
#                 if l <= query <= r:
#                     min_size = min(min_size, r-l+1)
#             result.append(min_size if min_size != float('inf') else -1)
#         return result

import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        res = [-1] * len(queries)
        heap = []
        i = 0
        for q, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, ((r-l+1), r))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[idx] = heapq.heappop(heap) 
        return res
