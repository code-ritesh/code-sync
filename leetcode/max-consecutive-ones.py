class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int c = 0;
        int max = 0;

        for(int x : nums){
            if(x == 1 ){
                c++;
                max = Math.max(c,max);
            }

            else c = 0;
        }

        return max;
    }
}