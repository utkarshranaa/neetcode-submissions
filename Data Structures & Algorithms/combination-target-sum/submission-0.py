class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        comb_sum = []

        def dfs(i, curr_target):

            if curr_target == 0:
                res.append(comb_sum.copy())
                return 
            if curr_target < 0 or i>=len(nums):
                return    
            
            comb_sum.append(nums[i])
            dfs(i, curr_target - nums[i])

            comb_sum.pop()
            dfs(i+1, curr_target)
        
        dfs(0, target)
        return res

        