'''
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
'''

'''
Can the elements be duplicates ?
Can there be a null value in the input?
'''

'''
k=3
1,2,3,4
min_heap

heap = 1,2,3,4
remove elements until size(heap) == k
heap = 2,3,4
3rd largest = top of heap = 2

add = 5
heap = 2,3,4,5
remove elements until size(heap) == k
heap = 3,4,5
3rd largest = top of heap = 3

add = -1
heap = -1,3,4,5
remove elements until size(heap) == k
heap = 3,4,5
3rd largest = top of heap = 3
'''

'''
Time: O(nlognk)
Space: O(n)
'''

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.min_heap, num)
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)