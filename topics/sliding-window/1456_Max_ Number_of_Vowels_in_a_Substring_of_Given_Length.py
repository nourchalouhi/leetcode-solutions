# Problem: 1456. Maximum Number of Vowels in a Substring of Given Length
# Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Pattern: Sliding Window
# Topic: String, Sliding Window
# Difficulty: Medium
# Time: O(n) - we process each character once
# Space: O(1) - constant space for the vowel set and counters

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Create a set of vowels for fast lookup
        vowels = set("aeiou")
        max_vowels = window_vowels = 0

        # Count vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                window_vowels += 1
        max_vowels = window_vowels

        # Slide the window through the string
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                window_vowels -= 1
            if s[i] in vowels:
                window_vowels += 1
            max_vowels = max(max_vowels, window_vowels)

        return max_vowels

# # Example usage:
# s = Solution()
# print(s.maxVowels("abciiidef", 3))  # Output: 3