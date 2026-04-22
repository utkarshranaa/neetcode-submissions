class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1= {}

        for i in range(len(nums)):
            
            dict1[nums[i]] = dict1.get(nums[i] , 0) +1
        
        for i in dict1.values():
            if i>1:
                return True
        return False