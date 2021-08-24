# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
 def lengthOfLongestSubstring(self, s: str)
    charSet=set()
        left=0
        result=0
        right=0
        while right< len(s):
            if s[right] not in charSet:
                charSet.add(s[right])
                result=max(result, right - left + 1)
                right+=1
            else:
                charSet.remove(s[left])
                left+=1
        return result
        

# 76.Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

    def minWindow(self, s: str, t: str) -> str:
        window, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        l = 0
        minLen = float('inf')
        minWin = [-1,-1]
        need = len(countT)
        have = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r-l+1
                    minWin = [l,r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        if minWin[0] == -1:
            return ""
        else:
            return s[minWin[0]:minWin[1]+1]
# 239.You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Example 3:

# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# Example 4:

# Input: nums = [9,11], k = 2
# Output: [11]
# Example 5:

# Input: nums = [4,-2], k = 2
# Output: [4]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        new_arr=[]
        max_num=deque()
        for i,n in enumerate(nums):
            while max_num and nums[max_num[-1]]<=n:
                    max_num.pop()
            max_num +=[i]
            if i-max_num[0]>=k:
                max_num.popleft()
            if i+1>=k:
                new_arr.append(nums[max_num[0]])
        return new_arr

# 713. Subarray Product Less Than K
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<1:
            return 0
        total=1
        count=0
        left=0
        for right in range(len(nums)):
            total=total*nums[right]
            while total >= k:
                total=total/nums[left]
                left+=1
            count+=right-left+1
        return count
