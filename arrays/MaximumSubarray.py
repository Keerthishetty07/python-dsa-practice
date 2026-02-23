"""
Problem: Maximum Subarray (LeetCode #53)
Topic: Arrays / Dynamic Programming
Pattern: Kadane's Algorithm (Running Sum + State Reset)

Time Complexity: O(n)
Space Complexity: O(1)

Insight:
Maintain a running sum. If extending the previous subarray reduces the sum,
restart from the current element instead.

Example Dry Run:
nums = [-2,1,-3,4,-1,2,1,-5,4]
Maximum subarray = [4,-1,2,1] → sum = 6
"""

def max_sub_array(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        # Decide to extend or restart
        current_sum = max(nums[i], current_sum + nums[i])

        # Track best sum
        max_sum = max(max_sum, current_sum)

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(nums))