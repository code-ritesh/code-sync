class Solution {
    public int findDuplicate(int[] nums) {
        HashMap <Integer , Integer> map = new HashMap<>();

        for(int x : nums){
            
            if( map.containsKey(x) ) return x;

            map.put(x , map.getOrDefault(x,0) + 1);
        }

        return -1;
    }
}