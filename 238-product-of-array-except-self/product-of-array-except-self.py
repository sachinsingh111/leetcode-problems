class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        prefix=1
        postfix=1
        for i in range(len(nums)):
            result.append(prefix)
            prefix*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            result[j]=result[j]*postfix
            postfix*=nums[j]
        return result


       



        