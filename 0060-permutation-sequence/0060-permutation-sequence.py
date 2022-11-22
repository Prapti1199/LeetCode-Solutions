class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        num = []
        ans = ""
        for i in range(1,n):
            fact = fact * i
            num.append(i)
        num.append(n)  
        k = k-1
        while(True):
            temp = int(k/fact)
            ans = ans + str(num[temp])
            num.remove(num[temp])
            if(len(num) == 0):
                break
            
            k = k%fact
            fact = fact/len(num)
        return ans
        