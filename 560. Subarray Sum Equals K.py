class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # current_sum − k = previous_prefix_sum 
        # lets us find subarrays ending at the current index that sum to k 
        # regardless of where they start.
        hashmap = {}
        hashmap[0] = 1
        r = 0
        sum = 0
        result = 0
        while r < len(nums):
            sum += nums[r]
            if sum-k in hashmap:
                result += hashmap.get(sum-k)
            hashmap[sum] = hashmap.get(sum, 0) + 1
            r += 1
        return result