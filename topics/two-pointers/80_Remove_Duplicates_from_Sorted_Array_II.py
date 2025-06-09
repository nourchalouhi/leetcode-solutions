# Problem: 80. Remove Duplicates from Sorted Array II
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Pattern: Two Pointers
# Topic: Array, Two Pointers
# Difficulty: Medium
# Time: O(n) - Each element is considered once.
# Space: O(1) - In-place algorithm with only constant extra space for pointers.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        leftIndex = 2  # Where the next allowed element should go

        # Start from index 2 since the first two elements are always allowed
        for rightIndex in range(2, len(nums)):
            # If current number is not the same as the element two places before,
            # it can be included
            if nums[rightIndex] != nums[leftIndex - 2]:
                nums[leftIndex] = nums[rightIndex]
                leftIndex += 1

        # leftIndex is the new length of the array with duplicates allowed at most twice
        return leftIndex

# Example usage:
# nums = [1,1,1,2,2,3]
# k = Solution().removeDuplicates(nums)
# print(k)         # Output: 5
# print(nums[:k])  # Output: [1, 1, 2, 2, 3]