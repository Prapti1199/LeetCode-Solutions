class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        for(int[] row : accounts){
            int sum = 0;
            for(int column : row){
                sum += column;
            }
            if (max < sum)
                max = sum;
        }
        return max;
    }
}