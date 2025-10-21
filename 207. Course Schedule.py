'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

'''
(0,1),(0,2),(1,2)
0->1,2
1->2
2->null

create a map: subject -> prereq
for each subject check prereq using dfs
if dept time is not set then it is cycle
if there is cycle then return false

how to find cycle ?
track arrival and dept time for each visited subject
if subject is visited and dept time is not assigned then there is a cycle

Time: O(n)
Space: O(n)
'''

class Solution:
    def is_cycle (self, course, hashmap, arr, dept):
        self.time += 1
        arr[course] = self.time
        for prereq in hashmap[course]:
            if (arr[prereq] == -1 and self.is_cycle(prereq, hashmap, arr, dept)):
                return True
            elif dept[prereq] == -1:
                return True
        self.time += 1
        dept[course] = self.time
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {}
        n = numCourses
        for i in range(n):
            hashmap[i] = []
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
        arr = [-1] * n
        dept = [-1] * n
        self.time = 0
        for i in range(n):
            if (arr[i] == -1 and self.is_cycle(i, hashmap, arr, dept)):
                return False
        return True