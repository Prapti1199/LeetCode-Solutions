class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        i = 0
        ans = ""
        while(True):
            if strs[0] == ans:
                return ans
            p = strs[0][i]
            for j in range(1,len(strs)):
                if i<len(strs[j]) and p == strs[j][i]:
                    continue
                else:
                    return ans
            ans += p
            i += 1
                    
            
                
            
        
        

            
    
            