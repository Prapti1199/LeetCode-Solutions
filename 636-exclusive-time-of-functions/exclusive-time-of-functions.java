class Solution {
    public static class Log{
        public int id;
        public boolean isStart;
        public int time;
        public int subDuration;

        public Log(String content){
            String[] strs = content.split(":");
            id = Integer.parseInt(strs[0]);
            isStart = strs[1].equals("start");
            time = Integer.parseInt(strs[2]);
            subDuration = 0;
        }
    }
    public int[] exclusiveTime(int n, List<String> logs) {
        Stack<Log> stk = new Stack<>();
        int[] result = new int[n];

        for(String s : logs){
            Log l = new Log(s);
            if(l.isStart){
                stk.push(l);
            } else {
                Log top = stk.pop();
                result[top.id] += (l.time - top.time + 1) - top.subDuration;
                if(!stk.isEmpty()){
                    stk.peek().subDuration += (l.time - top.time +1);
                }
            }
        }
        return result;
        
    }
}