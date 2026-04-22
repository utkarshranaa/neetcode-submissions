class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in dict1:
                return [min(dict1[pair], i) , max(dict1[pair], i)]
            else:
                dict1[nums[i]] = i
        