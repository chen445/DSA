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

 