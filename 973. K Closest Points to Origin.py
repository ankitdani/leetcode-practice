'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''

'''
If 2nd point distance > 1st point distance
x2**2 + y2**2 > x1**2 + y1**2

(1,2),(2,4)

5,20

(1,2),(2,-4)

5,20
'''

'''
Approach 1:
min heap 
add x**2 + y**2 in heap
result => pop until k > 0

Approach 2:
max heap if size of max heap > k then pop and remove max distance element =>  O(nlogk)
'''

'''
Time: O(nlogn)
Space: O(n)
'''

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = x**2 + y**2
            heapq.heappush(min_heap, (distance, x, y))
        result = []
        while len(min_heap) > 0 and k > 0:
            element = heapq.heappop(min_heap)
            result.append((element[1], element[2]))
            k -= 1
        return result