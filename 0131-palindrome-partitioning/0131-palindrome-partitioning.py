class Solution:
    def palindromePart(self, s, ans, ind, ds):
        if(ind == len(s)):
            ans.append(ds.copy())
            return
        
        for i in range(ind,len(s)):
            if(s[ind:i+1] == s[ind:i+1][::-1]):
                ds.append(s[ind:i+1])
                self.palindromePart(s,ans,i+1,ds)
                ds.pop()
            
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.palindromePart(s, ans, 0, [])
        return ans