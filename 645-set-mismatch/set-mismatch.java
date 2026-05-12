class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        Set<Integer> nset = new HashSet<Integer>();
        int currT = 0;
        int total = (n * (n+1))/2;

        for(int i: nums){
            nset.add(i);
            currT += i;
        }
        int sum = nset.stream().mapToInt(Integer::intValue).sum();
        System.out.println("Total : " + total);
        System.out.println("Sum : " + sum);
        System.out.println("CurrT : " + currT);

        int missing = total - sum;
        int repeat = currT - sum;

        return new int[]{repeat, missing};





        
    }
}