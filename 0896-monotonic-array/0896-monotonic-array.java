class Solution {
    public boolean isMonotonic(int[] nums) {
        
        if( nums.length == 1) return true;
        
        int j = 0;
        while(nums[j] == nums[j+1] && j<nums.length-2) j++;
        
        boolean decreasingSum = nums[j]>nums[j+1];
        boolean increasingSum = nums[j]<nums[j+1];
        
        
        for(int i=1; i<=nums.length-2; i++){
            
            if(nums[i]>nums[i+1] && increasingSum){
                return false;  
            }
            else if(nums[i]<nums[i+1] && decreasingSum){
                return false;
            }
        }
        
        return true;
        
    }
}