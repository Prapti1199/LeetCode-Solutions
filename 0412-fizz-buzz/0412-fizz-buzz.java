class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> results = new ArrayList<String>();
        for (int i=0; i<n; i++){
            if((i+1)%3 == 0 && (i+1)%5 == 0){
                results.add("FizzBuzz");
            }else if((i+1)%3 == 0){
                results.add("Fizz");
            } else if ((i+1)%5 == 0) {
                results.add("Buzz");
            }else {
                results.add(Integer.toString(i+1));
            }
            
        }
        return results;
    }
}