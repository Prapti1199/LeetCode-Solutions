class Solution {
    public int[] runningSum(int[] nums) {
        int sum = 0;
        int len = nums.length;
        int[] results = new int[len];
        results[0] = nums[0];
        for (int i=1; i<len; i++) {
            results[i] = results[i-1] + nums[i];
        }
        return results;
    }
}