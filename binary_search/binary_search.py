# 1.Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 def findMin( nums: List[int]) -> int:
        left, right=0, len(nums)-1
        while left < right:
            mid=left+(right-left)//2
            if nums[mid]>nums[right]:
                left 
            else:
                right=mid
        return nums[left]


# 2.This is an interactive problem.

# You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:

# returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
# returns 231 - 1 if the i is out of the boundary of the array.
# You are also given an integer target.

# Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: secret = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in secret and its index is 4.
# Example 2:

# Input: secret = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in secret so return -1.
#class ArrayReader:
#    def get(self, index: int) -> int:


   def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        left, right = 0,1
        while reader.get(right) < target:
            left=right
            right <<= 1 
        while left <= right:
            mid = (left + right) // 2
            if reader.get(mid)==target:
                return mid
            elif reader.get(mid)>target:
                right=mid-1
            else:
                left=mid+1
        return -1


# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
# Example 4:

# Input: nums = [1,3,5,6], target = 0
# Output: 0
# Example 5:

# Input: nums = [1], target = 0
# Output: 0

 def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            pivot = (left + right) // 2
            if target > nums[pivot]:
                left = pivot +1 
            else:
                right = pivot 
        return right

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_index = self.findIndex(nums,target,True)
        if first_index==-1:
            return [-1,-1]
        last_index=self.findIndex(nums,target, False)
        return[first_index,last_index]
    def findIndex(self, nums:List[int], target:int, isFirst:bool)->int:
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]== target:
                if isFirst:
                    if mid==start or nums[mid-1]!=target:
                        return mid
                    end=mid-1
                else:
                    if mid==end or nums[mid+1] != target:
                        return mid
                    start=mid+1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return -1

# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

 

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

 def search(self, nums: List[int], target: int) -> bool:
        left, right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid] ==target:
                return True
            if nums[mid]==nums[left]:
                left+=1
            elif nums[mid] > nums[left]:
                if nums[mid] > target and nums[left] <= target:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left=mid+1
                else:
                    right=mid -1
        return False

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


   def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left <= right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid] >= nums[left]:
                if target>=nums[left] and nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target<=nums[right] and nums[mid]< target:
                    left=mid+1
                else:
                    right=mid-1
        return -1
 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104


 

#  Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106




# Reach The end in time
def neigbors(grid, pos):
    possiblities = [
        (pos[0], pos[1]+1),
        (pos[0], pos[1]-1),
        (pos[0]+1, pos[1]),
        (pos[0]-1, pos[1]),
    ]
    r = []
    for neighbor in possiblities:
        if neighbor[0] >= 0 and neighbor[0] < len(grid) and neighbor[1] >= 0 and \
             neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == '.':
            r.append(neighbor)
    return r 

def reachTheEnd(grid, maxTime):
    # Write your code here
    if len(grid) == 0 or len(grid[0]) == 0:
        return "No"
    
    queue = [(0,0)]
    currentTime = 0
    visited = set()
    while len(queue) > 0 and currentTime <= maxTime:
        next_queue = []
        while len(queue) != 0:
            pos = queue.pop()
            if pos == (len(grid)-1, len(grid[0])-1):
                return "Yes"
            visited.add(pos)
            for neighbor in neigbors(grid, pos):
                if neighbor in visited:
                    continue
                next_queue.append(neighbor)
        queue = next_queue
        currentTime += 1
    return "No"     
        

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

 def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        while left<right:
            mid=left+(right-left)//2
            if self.cal_h(mid, piles) > h:
                left=mid+1
            else:
                right=mid
        return left
    
    
    def cal_h(self,k,piles):
        hour=0
        for pile in piles:
            if pile % k == 0: 
                hour+=pile //k
            else:
                hour+=pile//k+1
        return hour

# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# It is guaranteed that there will be an answer.

 

# Example 1:

# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
# Example 2:

# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44
# Example 3:

# Input: nums = [21212,10101,12121], threshold = 1000000
# Output: 1
# Example 4:

# Input: nums = [2,3,5,7,11], threshold = 11
# Output: 3
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# 1 <= nums[i] <= 106
# nums.length <= threshold <= 106

 def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left,right=1, max(nums)
        while left < right:
            mid=left+(right-left)//2
            if self.possible_divisor(nums,mid) <= threshold:
                right=mid
            else:
                left= mid+1
        return left 
        
    def possible_divisor(self, nums, divisor):
        total=0
        for num in nums:
            total+=math.ceil(num/divisor)
        return total
            

