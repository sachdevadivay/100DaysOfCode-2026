# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev1 = prev2 = 0
            for num in arr:
                prev1, prev2 = max(prev2 + num, prev1), prev1
            return prev1

        return max(helper(nums[:-1]), helper(nums[1:]))
