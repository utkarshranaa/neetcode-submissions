class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        comb_sum = []

        def dfs(i, curr_target):
            if curr_target == 0:
                res.append(comb_sum.copy())
                return 
            if curr_target < 0 or i>=len(candidates):
                return    
            
            comb_sum.append(candidates[i])
            dfs(i+1, curr_target - candidates[i])

            comb_sum.pop()

            while i+1<len(candidates) and candidates[i] == candidates [i+1]:
                i+=1

            dfs(i+1, curr_target)
        
        dfs(0, target)
        return res

        