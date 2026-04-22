class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        freq=[[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            dict1[nums[i]] = 1+ dict1.get(nums[i], 0) 

        for i , v in dict1.items():
            freq[v].append(i)
        ans=[]

        for i in range(len(freq)- 1, 0 , -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

             

        