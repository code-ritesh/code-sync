class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        return helper(nums,k) - helper(nums,k-1);
    }

    int helper(int[] nums, int k){
        int count = 0;
        int n = nums.length;
        int i = 0;
        int sum = 0 ;

        for(int j = 0 ; j < n ; j++){
            sum += (nums[j] % 2);

            while(sum > k ){
                sum -= nums[i] % 2;
                i++;
            }

            count += j-i+1;
        }

        return count;
    }
}