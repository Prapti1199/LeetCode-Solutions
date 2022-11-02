class Solution:
    def find(self, index, target, ans, ds, candidates):

        if index == len(candidates):
            if target == 0:
                ans.append(ds.copy())
                print("target is 0: ", ans)
            return ans
        if candidates[index] <= target:
            ds.append(candidates[index])
            print("ds take: ", ds, "  ",target)
            self.find(index,target-candidates[index],ans,ds,candidates)
            ds.pop()
        self.find(index+1,target,ans,ds,candidates)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.find(0, target, ans, [], candidates)
        return ans
