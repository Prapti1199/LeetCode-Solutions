class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        while len(v1)>len(v2):
            v2.append(0)
        while len(v2)>len(v1):
            v1.append(0)
            
        i = 0
        while i < len(v1):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v2[i]) < int(v1[i]):
                return 1
            else:
                i += 1
        
        return 0
                
            
            
            
        