# Problem: Two Sum (LeetCode #1)
# Approach: HashMap(dictionary) complement technique
# Time: O(n)
# Space: O(n)

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in hashmap:
                return [hashmap[need], i]

            hashmap[nums[i]] = i
