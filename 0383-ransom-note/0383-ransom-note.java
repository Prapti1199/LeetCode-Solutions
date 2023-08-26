class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> mLetters = new HashMap<Character, Integer>();
        for (int i = 0; i < magazine.length(); i++){
            char l = magazine.charAt(i);
            int count = mLetters.getOrDefault(l,0);
            mLetters.put(l, count+1);
    
        }
        
        for (int i= 0; i < ransomNote.length(); i++){
            char l = ransomNote.charAt(i);
            int count = mLetters.getOrDefault(l,0);
            if (count == 0){
                return false;
            }
            mLetters.put(l, count-1);
        }
    
        return true;
            
    }
}