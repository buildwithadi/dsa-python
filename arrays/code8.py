# 347. Top K Frequent Elements
# Medium
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

# Method 1 : (Time: O(n + dlogd) Space: O(d); n: size of array and d: count of distinct elements in array)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        res = list()

        for i in nums:
            if i in elements.keys():
                elements[i] = elements[i] + 1
            else:
                elements[i] = 1
        
        res = sorted(elements, key=elements.get, reverse=True)

        return res[0:k]