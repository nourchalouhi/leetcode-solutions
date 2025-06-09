# Problem: 643. Maximum Average Subarray I 
# Link: https://leetcode.com/problems/maximum-average-subarray-i/description/
# Pattern: Sliding Window
# Topic: Array, Sliding Window
# Difficulty: EASY
# Time: O(n)
# Space: O(1)


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Step 1: Initialise the window sum using the first k elements of the array
        maxSum=0
        windowSum=0
        for i in range (k):
            windowSum +=nums[i]
        # Step 2: Set the initial maximum sum to the sum of the first window
        maxSum = windowSum
        # Step 3: Set up the starting and ending indices of the sliding window
        startInd = 0
        endInd = k

        #Step 4: Calculating the sum with window sliding algorithm
        while endInd < len(nums):
            windowSum -= nums[startInd] 
            windowSum += nums[endInd]
            if maxSum < windowSum:
                maxSum = windowSum
        #Step 5: Updating positioning by sliding the window for the next calculation
            startInd+=1
            endInd+=1
     
        averageCalculated = maxSum /float (k) 

        return averageCalculated
