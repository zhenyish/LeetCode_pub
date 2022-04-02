class Solution(object):
    def searchInsert(self, nums, target):
        mid = len(nums)/2
        notUsesize = len(nums)
        while(mid > 0 or mid < len(nums)):
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                if(mid==0):
                    return mid
                notUsesize = mid
                mid = mid/2
            else:
                if((notUsesize-mid)/2 != 0):
                    mid = mid+(notUsesize-mid)/2
                else:
                    return mid+1
             
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
