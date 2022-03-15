# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false




class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True
        
        i = 0
        for c in t:
            if c == s[i]:
                i += 1   
                
            if i == len(s):
                break
                
        return i == len(s)