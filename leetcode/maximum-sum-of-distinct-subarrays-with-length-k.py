class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int n = nums.length;
        Map <Integer , Integer> map = new HashMap<>();
        long sum = 0;
        long maxsum = 0;

        for(int i = 0 ; i < n ; i++){
            int x = nums[i];

            sum += x;
            map.put(x , map.getOrDefault(x,0) + 1);

            // if we shrink the window
            if(i >= k ){
                int val = nums[i-k];
                sum -= val;

                map.put(val, map.get(val) -1 );

                if(map.get(val) == 0 ){
                    map.remove(val);
                }
            }

            // update the answer
            if(i >= k-1 && map.size() == k ){
                maxsum = Math.max(sum , maxsum);
            }

        }

        return maxsum;
    }
}