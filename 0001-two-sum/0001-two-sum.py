class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [] 
        for i in range(0,len(nums)):
                value = target - nums[i]
                print(value)
                if value in nums[i+1:]:
                    print(nums[i+1:])
                    ans.append(i)
                    ans.append(nums[i+1:].index(value)+i+1)
                    break
        return ans
            
      