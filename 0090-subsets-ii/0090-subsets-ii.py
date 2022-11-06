class Solution:
    def subsets(self, ind, ans, ds, c):
        ans.append(ds.copy())
        print(ans)
        for i in range(ind,len(c)):
            if(i != ind and c[i] == c[i-1]):
                continue
            ds.append(c[i])
            self.subsets(i+1,ans,ds,c)
            ds.pop()
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.subsets(0,ans,[],nums)
        return ans
        