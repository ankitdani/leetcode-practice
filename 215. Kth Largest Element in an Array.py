'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
'''

'''
Can the input be empty ?
'''

'''
k = 3 -> find 3rd largest 
1,2,3,4
result => 2

num = 1
minheap = 1

num = 2
minheap = 1,2

num = 3
minheap = 1,2,3

num = 4
minheap = 1,2,3,4
len(minheap) > k
pop
minheap = 2,3,4

result => top of heap = 2
'''

'''
min heap
add all elements in heap, remove largest element once size of heap is > k
result => top of the heap
Time: O(nlogk)
Space: o(k)
'''

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return heapq.heappop(min_heap)