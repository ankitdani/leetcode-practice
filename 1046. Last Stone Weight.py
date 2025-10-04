'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

'''

'''
Can the stones array be empty ?
What should be returned if there is only 1 stone throughput the input ?
'''

'''
max_heap
stones = 1,2,3,4
max_heap = 4,3,2,1

4-3=1 => take 2 largest stone, add difference back in heap until only 1 stone is in heap
max_heap = 2,1,1

2-1=1
max_heap = 1,1,1

1-1=0 both stones destroyed, no action
max_heap = 1 => result
'''

'''
Time: O(nlogn)
Space: O(n)
'''
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            max_heap.append(-stone)
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            diff = abs(stone1 - stone2)
            if diff != 0:
                heapq.heappush(max_heap, -diff) 
        return -max_heap[0] if max_heap else 0
        
