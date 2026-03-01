class Solution {
    public int minPartitions(String n) {
        int maxDigit = 0;

        for(int i=0; i<n.length(); i++){
            char c = n.charAt(i);
            int v = Character.getNumericValue(c);
            if(v > maxDigit){
                maxDigit = v;
            }
        }
        return maxDigit;
        
    }
}