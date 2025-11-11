'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. 
For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
'''

'''
ababcc
result=[4,2] (abab,cc)

1st pass
a->2
b->3
c->5

2nd pass
i=0
end=max(end,last index of a)=max(0,2)=2
i == end ? -> no

i=1
end=max(end,last index of b)=max(1,3)=3
i == end ? -> no

i=2
end=max(end,last index of a)=max(3,2)=3
i == end ? -> no

i=3
end=max(end,last index of a)=max(3,2)=3
i == end ? -> yes
update result -> 3-0+1 -> 4
start=end+1=3+1=4

i=4
end=max(end,last index of c)=max(3,5)=5
i == end ? -> no

i=5
end=max(end,last index of c)=max(4,5)=5
i == end ? -> yes
update result -> 5-4+1 -> 2 -> [4,2]
start=end+1=3+1=4

keep track of the last occurance of each letter and store in a dictionary
the last occurance is the the end of the partition

Time: O(n)
Space: O(1)
'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance_index_dict = {ch: i for i, ch in enumerate(s)}
        start = 0
        end = 0
        res = []
        for i, ch in enumerate(s):
            end = max(end, last_occurance_index_dict[ch])
            if i == end:
                res.append(end-start+1)
                start = end + 1
        return res