class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return helper(nums,k) - helper(nums,k-1);
    }

    int helper(int[] nums, int k){
        int count = 0;
        int n = nums.length;
        int i = 0;
        HashMap <Integer , Integer> map = new HashMap<>();

        for(int j = 0 ; j < n ; j++){
            
            map.put( nums[j] , map.getOrDefault( nums[j] , 0 ) + 1);

            while( map.size() > k ){
                map.put(nums[i] , map.getOrDefault(nums[i] , 0) - 1);

                if(map.get(nums[i]) == 0 ) map.remove(nums[i]);
                i++;
            }

            count += j-i+1;
        }

        return count;
    }
}