'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''

'''
dfs 
create a map: course -> prereq
if there is a cycle then it is impossible to finish all courses

How to check cycle ?
track arrival and dept time for each course
if course does not have dept time then it is impossible to reach the course

whenever we visit a course then add it to the result

Time: O(n)
Space: O(n)
'''

class Solution:
    def is_cycle (self, course, arr, dept, hashmap):
        self.time += 1
        arr[course] = self.time
        for prereq in hashmap[course]:
            if arr[prereq] == -1 and self.is_cycle (prereq, arr, dept, hashmap):
                return True
            elif dept[prereq] == -1:
                return True
        self.time += 1
        dept[course] = self.time
        self.result.append(course)
        return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        hashmap = {}
        for i in range(n):
            hashmap[i] = []
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
        arr = [-1] * n
        dept = [-1] * n
        self.time = 0
        self.result = []
        for i in range(n):
            if arr[i] == -1 and self.is_cycle (i, arr, dept, hashmap):
                return []
        return self.result