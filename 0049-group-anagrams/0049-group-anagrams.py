class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        
        for st in strs:
            print(st)
            sortedstr = " ".join(sorted(st))
            if sortedstr not in res :
                res[sortedstr] = []
            res[sortedstr].append(st)
        return list(res.values())
           
        