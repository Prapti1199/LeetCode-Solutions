class Solution(object):
    def helper(self, s):
        result = []
        pat = s[0]
        count = 1
        for i in range(1,len(s)) :
            if s[i] == pat:
                count +=1
            else : 
                result.append([str(count),pat])
                pat = s[i]
                count = 1
        result.append([str(count),pat])
        
        ans = ""
        for i in result :
            ans += str(i[0]) + str(i[1])
        print(ans)
        return ans
            
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        for i in range(1,n+1):
            if i == 1:
                s = "1"
            else:
                s = self.helper(s)        
        return s
                
        
   
           
            
            
            
            
        