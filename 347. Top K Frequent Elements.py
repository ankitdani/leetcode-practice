'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

'''
Can k be 0 ?
what to return if k > length of the input?
'''

'''
Approach 1 : 2 pass solution
Objective is to find k most frequent elements
use hashmap: element -> frequency
insert tuples like (frequency, element) in min heap
result => the top k elements in min heap
'''

'''
k = 2 => 
1,1,2,3,4

2 most frequent => 1,2

heap = (2,1), (1,2), (1,3), (1,4)

result => 1,2
'''

'''
Time: O(nlogk)
Space: O(n)
'''
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        max_heap = []
        for num, freq in hashmap.items():
            heapq.heappush(max_heap, (freq, num))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        result = []
        for freq, num in max_heap:
            result.append(num)
        return result