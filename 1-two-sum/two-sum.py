class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap={}
        for i ,n in enumerate(nums):
            diff=target-n
            if diff in preMap:
                return [i,preMap[diff]]
            preMap[n]=i




        