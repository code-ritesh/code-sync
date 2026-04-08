class Solution {
    public int[] singleNumber(int[] nums) {
        int[] res = new int[2];
        Map <Integer , Integer> map = new HashMap<>();
        int i = 0;

        for(int x : nums){
            map.put(x , map.getOrDefault(x,0) + 1);
        }

        for(int key : map.keySet()){
            int val = map.get(key);

            if(val == 1){
                res[i++] = key;
            }
        }

        return res;
    }
}