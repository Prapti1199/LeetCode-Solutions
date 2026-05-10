class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] sorted = Arrays.copyOf(nums, nums.length);
        int[] ans = new int[nums.length];
        Arrays.sort(sorted);

        System.out.println(" nums :" + nums[0]);

        for(int i=0; i<nums.length; i++){
            System.out.println("For num : " + nums[i]);
            int low = 0;
            int high = nums.length - 1;
            int idx = 0;
            int target = nums[i];

            while(low <= high){
                int mid = low + (high - low )/2;
                System.out.println("Mid : " + mid);

                if(sorted[mid] > target){
                    high = mid - 1;
                } else if (sorted[mid] < target){
                    low = mid + 1;
                } else{
                    idx = mid;
                    System.out.println("Got idx : "+ idx);
                    break;
                }

            }
            while(idx -1 >= 0 && sorted[idx -1] == target){
                    idx--;
            }


            ans[i] = idx;
            

        }
        return ans;
        
    }
}