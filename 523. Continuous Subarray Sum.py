class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if remainder of 2 numbers is 0 then good subarray
        # hashmap to store remainder -> index , subarray must be atleast 2 in length
        n = len(nums)
        index_map = {0: -1}
        prefix_sum = 0
        for i in range(n):
            prefix_sum += nums[i]
            remainder = prefix_sum if k == 0 else prefix_sum % k
            if remainder in index_map:
                if i - index_map.get(remainder) > 1:
                    return True
            else:
                index_map[remainder] = i
        return False
        
# Time: O(n)
# Space: O( min (n, k) )