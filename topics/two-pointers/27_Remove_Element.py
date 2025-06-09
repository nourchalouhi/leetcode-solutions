# Problem: 27. Remove Element
# Link: https://leetcode.com/problems/remove-element/
# Pattern: Two Pointers
# Topic: Array, Two Pointers
# Difficulty: Easy
# Time: O(n) - We look at each element of the array once.
# Space: O(1) - We use only a small, fixed amount of extra space (just the variable k).

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Step 1: Start a counter for non-val numbers
        k = 0

        # Step 2: Loop through each number in the array
        for i in range(len(nums)):
            # If the current number is NOT the value to remove
            if nums[i] != val:
                nums[k] = nums[i]  # Place it at the next position at the front
                k += 1             # Move the position for the next valid number

        # Step 3: k is now the number of elements not equal to val
        return k

# Example usage:
# nums = [3, 2, 2, 3]
# val = 3
# result = Solution().removeElement(nums, val)
# print(result)  # Output: 2
# print(nums[:result])  # Output: [2, 2]