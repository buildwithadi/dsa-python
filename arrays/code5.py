# 242. Valid Anagram
# Easy
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


# My Method: (Time: O(n), Space: O(1))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        check_s = dict()
        check_t = dict()

        for i in s:
            if i not in check_s:
                check_s[i] = 1
            elif i in check_s:
                check_s[i] += 1
        
        for i in t:
            if i not in check_t:
                check_t[i] = 1
            elif i in check_t:
                check_t[i] += 1

        for i in check_s:
            if check_s[i] != check_t[i]:
                return False
         
        return True    
    

# Similar but Simple Approact
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         count = defaultdict(int)
        
#         # Count the frequency of characters in string s
#         for x in s:
#             count[x] += 1
        
#         # Decrement the frequency of characters in string t
#         for x in t:
#             count[x] -= 1
        
#         # Check if any character has non-zero frequency
#         for val in count.values():
#             if val != 0:
#                 return False
        
#         return True