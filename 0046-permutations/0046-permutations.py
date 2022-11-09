class Solution:
    def recursion(self, nums, ds, nmap, ans):
        if len(ds) == len(nums):
            ans.append(ds.copy())
            return
        
        for i in range(0,len(nums)):
            if not nmap[i] :
                nmap[i] = True
                ds.append(nums[i])
                self.recursion(nums, ds, nmap, ans)
                ds.pop()
                nmap[i] = False
            
        
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        nmap = [0]*len(nums)
        ans = []
        self.recursion(nums, [], nmap, ans)
        return ans
        