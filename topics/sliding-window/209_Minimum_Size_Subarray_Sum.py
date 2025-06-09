# Problem: 209. Minimum Size Subarray Sum
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/
# Pattern: Sliding Window
# Topic: Array, Binary Search, Sliding Window, Prefix
# Difficulty: Medium
# Time:O(n) - both left and right pointers move forward at most n times
# Space: O(1) - uses constant extra space regardless of input size

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        minWindowSize = n + 1  # Start with a value greater than any possible window

        windowSum = 0
        windowSize = 0
        left = 0

        # Step 1: Begin iterating through the array using the right pointer
        for right in range(n):

            # Step 2: Add the current element to the running window sum
            windowSum += nums[right]

            # Step 3: While the current window sum meets or exceeds the target
            while windowSum >= target:

                # Step 4: Calculate the current window size
                windowSize = right - left + 1

                # Step 5: If it's smaller than the smallest found so far, update minWindowSize
                if windowSize < minWindowSize:
                    minWindowSize = windowSize

                # Step 6: Shrink the window from the left by subtracting the leftmost element
                windowSum -= nums[left]
                left += 1

        # Step 7: After processing, check if a valid window was ever found
        if minWindowSize == n + 1:
            return 0
        else:
            return minWindowSize
