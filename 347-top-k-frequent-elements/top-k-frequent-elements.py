class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for i in range(len(nums)+1)]
        count={}
        for i in nums:
            count[i]=count.get(i,0) +1
        for key, value in count.items():
            freq[value].append(key)
        result=[]
        for n in range(len(freq)-1,0,-1):
            for j in freq[n]:
                result.append(j)
                if len(result)==k:
                    return result
                






       