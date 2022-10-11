class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        st = s.split()
        print(st)
        l = 0
        r = len(st)-1
        
        while l <= r :
            st[l], st[r] = st[r], st[l]
            l += 1
            r -= 1
            
        ans = " ".join(st)
        return ans
        
        