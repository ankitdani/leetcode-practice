'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
'''

'''
aab
result=aba

aaa
result=""

take the most frequent letter and add it to result
decrement freq and add back to max heap

pass 1
calculate frequency of each letter and store in max heap
max heap = (2,a),(1,b)

pass 2
max heap = (2,a),(1,b)
result = ""

max heap = (1,b),(1,a)
result = a

max heap = (1,a)
result = ab

max heap = 
result = aba

Time: O(nlogk) -> k letters
Space: O(n)
'''
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_heap = [(-freq, ch) for ch, freq in freq.items()]
        heapq.heapify(max_heap)
        
        res = ""
        prev = None
        while max_heap:
            freq, ch = heapq.heappop(max_heap)
            freq += 1
            res += ch
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if freq != 0:
                prev = (freq, ch)
        return res if prev is None else ""