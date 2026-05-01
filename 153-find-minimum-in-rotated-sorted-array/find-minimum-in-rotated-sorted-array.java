class Solution {
    public int findMin(int[] arr) {
        int low = 0;
        int high = arr.length - 1;
        int lowest = Integer.MAX_VALUE;

        while(low <= high){
            int mid = (low + high)/2;
            lowest = Math.min(lowest, arr[mid]);

            if(arr[low] <= arr[mid]){

                lowest = Math.min(lowest, arr[low]);
                low = mid + 1;
            } else{
                lowest = Math.min(lowest, arr[high]);
                high = mid - 1;

            }
            
        }
        return lowest;

        
    }
}