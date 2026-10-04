class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left=[1]*len(nums)
        right=[1]*len(nums)

        #left products
        #left=[1,1,2,8]
        #right=[48,24,6,1]
        [1,1,2,1]
        for i in range(1,len(nums)):
            left[i]=nums[i-1]*left[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i]=nums[i+1]*right[i+1]

        result=[1]*len(nums)
        for i in range(len(nums)):
            result[i]=left[i]*right[i]
        return result

            

            
