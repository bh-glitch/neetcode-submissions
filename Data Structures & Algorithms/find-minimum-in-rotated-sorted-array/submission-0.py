class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while left<right:
            mid = left+(right - left)//2
            
            #unsorted part is to the right
            if (nums[mid]>nums[right]):
                left = mid+1
            #unsorted part is to the left
            else:
                right = mid
        mid = left+(right - left)//2
        return nums[mid]
        
        


