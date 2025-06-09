# Problem: 424. Longest Repeating Character Replacement
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/
# Pattern: Sliding Window
# Topic: Hash Table, String, Sliding Window
# Difficulty: Medium
# Time: O(n) - Each character is added and removed from the window at most once, so the window slides across the string in a single pass.
# Space: O(1) - The count dictionary stores at most 26 English uppercase letters, so space usage is constant.

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        Time Complexity: O(n)
        - Each character is visited at most twice (once by right, once by left)
        - maxFreq is updated in O(1)
        - Entire loop runs in linear time relative to string length

        Space Complexity: O(1)
        - Dictionary holds at most 26 keys (A-Z), so space is constant
        """

        # Step 1: Initialise variables
        count = {}          # Frequency map to count letters in the current window
        left = 0            # Left pointer of the sliding window
        maxLen = 0          # Result to store the longest valid window
        maxFreq = 0         # Track the most frequent character count in the window

        # Step 2: Expand the window using the right pointer
        for right in range(len(s)):
            char = s[right]

            # Step 3: Add current character to the frequency map
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

            # Step 4: Update maxFreq to reflect the most frequent character in the window
            maxFreq = max(maxFreq, count[char])

            # Step 5: Calculate how many characters need to be replaced
            character_to_replace = (right - left + 1) - maxFreq

            # Step 6: If replacements needed > k, shrink the window from the left
            while character_to_replace > k:
                leftChar = s[left]
                count[leftChar] -= 1
                left += 1

                # Step 6.1: Recalculate character_to_replace with updated window size
                character_to_replace = (right - left + 1) - maxFreq

            # Step 7: Update maxLen with the size of the current valid window
            windowSize = right - left + 1
            maxLen = max(maxLen, windowSize)

        # Step 8: Return the length of the longest valid substring
        return maxLen