class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # If prefix sum is found before in hashmap then sum is equal 
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        hashmap = {0: -1}
        prefix_sum = 0
        max_len = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum in hashmap:
                max_len = max(max_len, i - hashmap.get(prefix_sum))
            else:
                hashmap[prefix_sum] = i
        return max_len

# Time: O (n)
# Space: O (n)