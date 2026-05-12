class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length;
        List<Integer> ans = new ArrayList<Integer>();
        Set<Integer> nSet = new HashSet<Integer>();
        for(int i: nums){
            nSet.add(i);
        }

        for(int i=1; i<=n; i++){
            if(!nSet.contains(i)){
                ans.add(i);
            }
        }

        return ans;
        
    }
}