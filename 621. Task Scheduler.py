'''
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.
'''

'''

'''

'''
n = 2
A,B,B

B,A,null,B
result => 4

store (frequency, letter) as tuple in maxheap

ch = A
maxheap = 1,A

ch = B
maxheap = (1,A),(1,B)

ch = B
maxheap = (2,B),(1,A)

improvement : instead of storing letters, we can only store frequencies
decrement freq and add back again in heap
create a queue and check the time when letter/freq can be used
next time = curr time + n

time = 0
heap = 2,1
q = null

time = 1
next time = heap top(2) + 2 = 4
curr = 2 decrement -> 1 add in heap and q
q = (1,4)
heap = 1,1 -> push in q only if curr time = q top time

time = 2
curr = 1 decrement -> 0
next time = null since curr == 0 after decrement
q = (1,4)
heap = 1

time = 3
check if top of q is same as curr time 
time ++
q = (1,4)
heap = 1

time = 4
top q time == curr time then pop and decrement
q[0]-- 
heap = nul

Time: O(nlogn)
Space: O(n)
'''
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        queue = deque()
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1
        max_heap = []
        for task, freq in hashmap.items():
            max_heap.append(-freq)
        heapq.heapify(max_heap)
        time = 0
        while max_heap or queue:
            time += 1
            # process most frequent
            if max_heap:
                freq = heapq.heappop(max_heap) 
                freq = freq +1
                if freq < 0:
                    next_time = time + n
                    queue.append((freq, next_time))
            if queue and time == queue[0][1]:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time