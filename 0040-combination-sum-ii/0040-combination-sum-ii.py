class Solution:
    def findSum(self, index, candidates, target, ans, ds):
        if(target == 0):
            ans.append(ds.copy())
            return 
        for i in range(index,len(candidates)):
            if i > index and candidates[i] == candidates[i-1]: continue
            if candidates[i]>target : break
            
            ds.append(candidates[i])
            self.findSum(i+1, candidates, target-candidates[i], ans, ds)
            ds.pop()
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.findSum(0, candidates, target, ans, [])
        return ans
        