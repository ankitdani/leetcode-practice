'''
Docstring for 134. Gas Station
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
'''

'''
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]

if total gas < total cost
then return -1

+gas-cost at each station
if at any point gas<0
then reset gas=0 and start from next station

Time: O(n)
Space: O(1)
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_gas < total_cost:
            return -1
        
        start = 0
        current_gas = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                start = i + 1

        return start