class Solution {
    public boolean areSimilar(int[][] mat, int k) {
        int r = mat.length;
        int n = mat[0].length;

        k %= n;
        for(int i=0; i<r; i++){
            for(int j=0; j<n; j++){
                if(i%2 == 0 && (mat[i][j] != mat[i][(j + k) % n])){
                    return false;
                }else if(mat[i][j] != mat[i][(j - k + n) % n]){
                    return false;
                }
            }
        }
        return true;
        
    }
}