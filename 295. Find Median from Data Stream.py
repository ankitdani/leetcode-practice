'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''

'''
2 heaps - max heap and min heap
max heap stores smaller half
min heap stores larger half

2,3,4

num = 2
if len of max heap == len of min heap then median is top of both / 2
else last element of max heap is median 

max heap = null 
max heap = -2
min heap = null
max heap = null
min heap = 2

num = 3
max heap = null
min heap = 2,3
len (min heap) > len(max heap) pop from min heap
max heap = -2
min heap = 3

median = top of max heap + top of min heap / 2 = 2.5

num = 4
max heap = -2,-4
min heap = 3

median = 3

'''

'''
Time: O(logn)
Space: O(n)
'''

import heapq

class MedianFinder:

    def __init__(self):
        self.heap1 = [] # max heap = stores lower half
        self.heap2 = [] # min heap = stores upper half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap1, -num)
        heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
        if len(self.heap2) > len(self.heap1):
            heapq.heappush(self.heap1, -heapq.heappop(self.heap2))

    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            return (-self.heap1[0] + self.heap2[0]) / 2.0
        return -self.heap1[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()