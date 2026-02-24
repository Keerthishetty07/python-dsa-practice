# Problem: Merge Intervals (LeetCode #56)
# Topic: Arrays + Sorting
# Pattern: Interval Merging (Sort + Greedy)
# Time: O(n log n)
# Space: O(n)

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Step 1: Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])

    merged = []

    # Step 2: Traverse intervals
    for interval in intervals:

        # If no overlap → add new interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)

        # Overlap → merge with last interval
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Example run

intervals = [[1,3], [2,6], [8,10], [15,18]]
print("Merged intervals:", merge(intervals))
