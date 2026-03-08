class Solution {
    public int numSpecial(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[] rowsOne = new int[rows];
        int[] colsOne = new int[cols];
        int result = 0;

        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                if(mat[i][j] == 1){
                    rowsOne[i] += 1;
                    colsOne[j] += 1;
                }
            }
        }

        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                if(mat[i][j] == 1 && rowsOne[i] == 1 && colsOne[j] == 1){
                    result += 1;
                }
            }
        }

        return result;

        
    }
}