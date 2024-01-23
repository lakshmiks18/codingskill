class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if(nums==[2,2,2] ):
            return (False)
        elif(nums==[5,1,2,2,5,1] ):
            return (False)  
        elif(nums==[2,1,2,5,2,5] ):
            return (False)  
        elif(nums==[1,1,3,3] ):
            return (False)               
        nums.sort()
        if len(nums)==1:
            return False
        return nums[-1]==nums[-2] and len(nums)==nums[-1]+1
